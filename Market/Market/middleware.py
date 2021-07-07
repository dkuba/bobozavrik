class SwitchMobileMiddleware:
    # middlewere для переключения на моб. мерсию сайта для пользователей зашедших с моб.
    def __init__(self, get_response):
        self._get_response = get_response
        
    def __call__(self,request):
        response = self._get_response(request)
        return response
    
    def process_template_response(self, request, respose):
        # определяем с какого устройства зашёл пользователь
        agent = request.META['HTTP_USER_AGENT']

        if 'Android' in agent or 'iPhone' in agent:
            # если зашли с моб. тел. : передаём в темплейты доп. аргумент который активизирует моб. версию. 
            respose.context_data["mobile"] = 'mobile versin'
            return respose
        else:
            return respose


