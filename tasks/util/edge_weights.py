import graph_tool.stats as gts
import json

SMALL_VALUE = 1*10**-10

def _calc_score(g, e, label, graph_key):
    if label is not None:
        # consider label score
        source = 1 if g.vertex_properties["type"][int(e.source())] == 'Drug' else \
            g.vertex_properties[graph_key][int(e.source())][label.name]
        target = 1 if g.vertex_properties["type"][int(e.target())] == 'Drug' else \
            g.vertex_properties[graph_key][int(e.target())][label.name]

        # source + target is on average 1 since it is normalized
        # score can be 0 if unknown
        if source is None or source == 0.0:
            source = SMALL_VALUE
        if target is None or target == 0.0:
            target = SMALL_VALUE
    else:
        # no score, set it do default values
        source = 0.5
        target = 0.5
    return source, target

def _calc_hub_penalty(g, hub_penalty, avdeg, weights, inverse):
    hub_penalty_weights = {}
    for e in g.edges():
        edge_avdeg = float(e.source().out_degree() + e.target().out_degree()) / 2.0
        penalized_weight = (1.0 - hub_penalty) * avdeg + hub_penalty * edge_avdeg
        if inverse:
            hub_penalty_weights[e] = 1.0 / penalized_weight
        else:
            hub_penalty_weights[e] = penalized_weight
    # normalize hub penalty weights
    m = max(hub_penalty_weights.values())
    hub_penalty_weights_list = [float(i)/m for i in hub_penalty_weights.values()]
    # update weights
    for i, e in enumerate(hub_penalty_weights):
        weights[e] *= hub_penalty_weights_list[i]
    return weights

def edge_weights(g, hub_penalty, mutation_cancer_type=None, expression_cancer_type=None, 
                 tissue=None, inverse=False):
    """[summary]

    Args:
        g (graph_tools.Graph): [description]
        hub_penalty (float): penalty for hubs in range from 0 to 1
        mutation_cancer_type (str, optional): if set, we consider the mutation score of this cancer type
        expression_cancer_type ([type], optional): [description]. Defaults to None.
        inverse (bool, optional): [description]. Defaults to False.

    Raises:
        ValueError: [description]

    Returns:
        [type]: [description]
    """
    avdeg = gts.vertex_average(g, "total")[0]
    weights = g.new_edge_property("double", val=avdeg)    
    if hub_penalty > 1:
        raise ValueError("Invalid hub penalty {}.".format(hub_penalty))
    # skip iterating through network if not needed to speed up
    if mutation_cancer_type is not None or expression_cancer_type is not None or tissue is not None:

        if hub_penalty < 0:
            hub_penalty = 0

        for e in g.edges():
            
            edge_avdeg = float(e.source().out_degree() + e.target().out_degree()) / 2.0
            
            # Mutation weights
            mut_source, mut_target = _calc_score(g, e, mutation_cancer_type, 'mutation_scores')
            # Expression weights
            expr_source, expr_target = _calc_score(g, e, expression_cancer_type, 'cancer_expression_scores')
            # Tissue Expression weights
            texpr_source, texpr_target = _calc_score(g, e, tissue, 'expression_scores')

            penalized_weight = (1.0 / (mut_source + mut_target)) * (1.0 / (expr_source + expr_target)) * \
            (1.0 / (texpr_source + texpr_target)) * ((1.0 - hub_penalty) * avdeg + hub_penalty * edge_avdeg)

            if inverse:
                weights[e] = 1.0 / penalized_weight
            else:
                weights[e] = penalized_weight

    if hub_penalty > 0:
        # add hub penalty
        weights = _calc_hub_penalty(g, hub_penalty, avdeg, weights, inverse)
    
    return weights
