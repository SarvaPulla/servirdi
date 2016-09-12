from tethys_sdk.base import TethysAppBase, url_map_maker


class ServirCatalog(TethysAppBase):
    """
    Tethys app class for Servir Catalog.
    """

    name = 'Servir Water Observations Data Integrator'
    index = 'servir:home'
    icon = 'servir/images/servir.png'
    package = 'servir'
    root_url = 'servir'
    color = '#004de6'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='servir',
                           controller='servir.controllers.home'),
                    UrlMap(name='add-server',
                           url='servir/add-server',
                           controller='servir.controllers.add_server'),
        )

        return url_maps