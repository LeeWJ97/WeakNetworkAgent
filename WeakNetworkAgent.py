from baseproxy.proxy import ReqIntercept,RspIntercept, AsyncMitmProxy
import time

class ImageInterceptor( ReqIntercept,RspIntercept):
    def deal_request(self, request):
        if ('/api/xxxxxxxxxxxx' in request.path):
            time.sleep(5)

        if ('/api/yyyyyyyyyyyy' in request.path):
            time.sleep(10)

        return request
    def deal_response(self, response):
        try:
            if  ('zzzzzzz' in response.get_body_data().decode('utf8')) or('aaaaaa' in response.get_body_data().decode('utf8')):
                time.sleep(10)
        except:
            pass
        return response


if __name__ == "__main__":
    baseproxy = AsyncMitmProxy(https=True,server_addr=('', 8080))
    baseproxy.register(ImageInterceptor)
    baseproxy.serve_forever()