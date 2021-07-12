import requests
import os
import random
import string
import json
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://accounts.google.com/_/lookup/accountlookup?hl=en-GB&_reqid=235521&rt=j'
response = requests.get(url)
names = json.loads(open('names.json').read())
while True:
 for name in names:
     
 	name_extra = ''.join(random.choice(string.digits))
 
 	email = name.lower() + name_extra + '@gmail.com'
 	password = ''.join(random.choice(chars) for i in range(8))
 
 	requests.post(url, headers=headers, allow_redirects=False, data={
   'ifkv': 'AU9NCczII-sSY_gGdfPp0KM1TIfceqXXj3N5m2nDjQeBriz_uAcwRQB23sdzXBQkd3MqUr08Bjed',
   'continue': 'https://accounts.google.com/ManageAccount?nc=1',
   'f.req': '["{'+ email +'}","AEThLlwejQzAIjgB1vyTcw15ykW8XO_r76W0KHbdDKi78JIXqf1_Dnlp8gCF1Ego6F0WJOCCImXkizneycDMIxhmjsravDeT2k8UtLX95gLsl5pCATk1IDqE7vaj1lZ8hVB1EzM7mY_uI2Y-2zsQsTbvmZ9ZtPlp2EhJmWyFFAQRK5D8sHHfZOQngETVfgdx4YnzD0_tX151XKZkeWEv_-f9TK38KLkUgDL_dKeV4Fk8kEZZ-FRYfD8CCT9u3w-uZhBFNnCc1Oo8",[],null,"ZA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin",null,[],4,[],"GlifWebSignIn",null,[]],1,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true,null,null,null,null,null,null,null,null,[]],"' + email + '",null,null,null,true,true,[]]',
   'bgRequest': '["identifier","<W5dql9oCAAbaF-s32heN2ghabob2Dtb0ACkAIwj8Ru5CX51k1W9cJEvW00gIfsP_uT-agzruFsHcPk0ZrBeeKXeclc0AAAGfnQAAABKnAQdWBLOULBZJp_I15AkL8ehAPRbMDYN4YqwmGAjY9JuLac3OPcsp3jEhZTCNy0Yk9iSESBRfUoLLvmpj7lsTROcZq5ywur4vknM3OfDuOKbfBnS0KHbtQETf_yofa0yd3P0ROX4A_IHB4OnSjqBrpe-Y7hFJ8fqqLUsg2QWMZTgWZk16_r5cQasiNguxe3IMKP5E0NBID26L4PADLQEy1MltKnKRxqCoYAutAqHuKn51FPu8Jf1QMceHfcDwNXhDBJUyXT5-BqObUkrSf83hjslyMB-8fDqyu8VjLNVsQ9Xo-VWm18jWPt8oEBEv8SLGvIn_YHhyq5hka7zdbQQuzu4jwCL3L3Uo1KxBhh_2PuJeIyAG6NVqb0a7709gR4_zdj3kI8XFCWm6cT8YgwL9V6xiIo_U7yu8IJjzGRV3kcbi63Xu7ARRZkmtrTu2pdQZM3-qssiVeBZ2dyWFAp57vSOfedd76qEHYa0f8iMcFsnkFByjL-3xT6zeonR4zbNN4pgyTFjxQDOrM0Zb1od4ELimARYnEP4yAY0f0Gnh3B6LCILJzuaAiE2ryEaj0B1rG4znXN27WRWVpRTf_qoLiCZI78ZK4IulP8hODUDbI19N4pPIjXnzoFKKUSI7l5c8SPCNlgMmnHWEKqNAbGQvUBapJeslc_TeqXeK4BoU5D5sNjwEqZq3XXOMLmD_JRQNPHtdjWlSWN0mR6YpIdo4-A6uM__vLRzOZx1Dw_4Yn4_c4x22JYf_QVmHV839jK9LoJ5AN0Jyp7GzmcbDGchXMH6AF6IYG2ZhNzrkQqv41xABdRVaABhoXEdJ0x4_UQiqxa075qSZfBpnPJtlMz-1ljIJVUdxdPNotZ6YjHmZhZgebncld2sucpvmpGiS3nwA2xUy5jh7s1AyBdvi7yMGc4g6UUHltkwPafnv6Vts25ITWCje4x3lsMgAHhw2VY1sGpW-9lNQ98M0qSpEW_0RsEN7IXJqalmUWyB8CcPJcWDl8TQCwrWr_02skI71t8oDTwTiSrRNFsXEIca6Rk_CFRUJAvk3xMW-cK_xatiH61riI7kqSc8lJdhRNKgs2DmtBItiPFkk5g1dS3thvz5ep7BpWNFRgZfBSkxU5VHTeChAO0A3oJsUKzVCrmdAMiyS8i7EyXAcM_h46rdBUq5-j9riVGKZCqJQ72HFje774ApjM70YJHBzG2eFwjr0pxWARYhwA_RCxyme03dsEEYs02xfBIBZmcMQSJ5SkUwFmGE50SBuZL2LjNzbscVbU7HAH60ydnBFKtuVt5BTGKDkX-2IjkXpaf1EbBf28tL0JbhrqGp-P8_v_7aRVczftXzphbeDPnKQWUvBKn7WkdghcepnOWy0_BCanGs6H7p4Qfnm6EqI3_Zrx4SOAZjuOa_C3IZlnnz7l5yAIK4EfToMQLBLZ8VnX0z-ifZA3BQnLr2HPOnmIlNnttL-1_HESOfJNbRsjAxJPHods4qJrsHqMPUh-ajBjEZKLVXs4kvslCozqz-HPsSAMG7p2Oh9U4v4DrHvt8xx7jo_kWppgVO_ppWWW95k50cbDK7KMbVY7XnGesRbtV438kkeSvhyUr0Z7RmQzkW3BVQ"]',
   'azt': 'AFoagUWSoEb2PC8RwuZWCz5Fxq3dVw8KIQ:1626076263248',
   'cookiesDisabled': 'false',
   'deviceinfo': '[null,null,null,[],null,"ZA",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false,1,""]',
   'gmscoreversion': 'undefined',
   'checkConnection': 'youtube:669:0',
   'checkedDomains': 'youtube',
   'pstMsg': '1'
 	})
 
 	print(f'sending {email} and {password} {response}\n') 
 
