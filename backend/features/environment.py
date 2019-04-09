def before_feature(context, feature):
    context.base_url = context.config.userdata['URL']


def before_scenario(context, scenario):
    pass