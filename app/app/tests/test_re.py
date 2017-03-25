#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_re.py
@time: 2016/10/11 下午5:49
"""

import re


def test_01():
    test_str = """
    <script type="text/javascript">
    try{
        var ____json4fe = {"catentry":[{"dispid":"8512","name":"家政服务","listname":"shenghuo"},{"dispid":"168","name":"保洁清洗","listname":"baojie"}],"locallist":[{"dispid":"2","name":"上海","listname":"sh"}],"start":(new Date()).getTime(),"modules":"list"};
        ____json4fe.version = 'A';
        ____json4fe.modules = 'listpage';
        ____json4fe.sid = '196213900193485617909111756';
        ____json4fe.sessionid = '1ff32794-2173-43ea-b9d7-330c79227b5e';
        ____json4fe.smsc = '3f2dd2de9529e633efce32a43f91939b4248a1cb97661fd33d14e492ef4d3fc877cc4a4b45acdad182cd8576cdd9299aa5d221668544a6c23e57e10697a20b4fa08339db11b066f281d5e4ec106f44b93b4fdec9a40f8495fe6a5777cdbb956980a271ca1f38159621ad07a421472ac20650f14203fd57914a72211677fb7279451da21146f28fdd45de07ab96feacf065f171f96fb00a8f0b1fabd3d042a45554b3ec0e2f57bcd99deb1dd7e3209ecd';
        ____json4fe.newcateid='';
        ____json4fe.keyword='';
        ____json4fe.page='8';
        ____json4fe.param='';
        }catch(e){};
        (function(){
    var e = "header,nav,section,aside,article,footer".split(','),
    i=0,
    length=e.length;
    while(i<length){
        document.createElement(e[i++])
    }
    })();
        var ajax_param = '{"pageIndex":8,"infoMethod":["renzheng","wltAge"],"platform":"pc","paramMap":null,"dispCateId":168,"dataParam":"25382785095096_38061562321175_0_adsumplayinfo,26860222294327_40165314644754_0_adsumplayinfo,27414855791424_41820219278351_0_adsumplayinfo,420993450305916928_23717694852358_3_adinfo,23852375233973_34187728876555_0_adinfo,26986608591686_26089533770758_0_promationinfo,25953371501738_38982245142801_0_promationinfo,25371970814137_38061562321175_0_promationinfo,27047834466749_41329382807566_0_promationinfo,27269340740039_6142467416839_0_promationinfo,26496124245819_40181378817550_0_promationinfo,26201512060610_25409956098310_0_promationinfo,27006744256178_9173524205063_0_promationinfo,27418039337775_24409104727815_0_promationinfo,25290858650426_37881741694993_0_promationinfo,27615431005119_40778953127698_0_promationinfo,25803997057981_38807365873687_0_promationinfo,27415563687758_41040430687507_0_promationinfo,25336113757896_23851185_0_promationinfo,27220545657022_41326207724050_0_promationinfo,27074330826300_40071910592782_0_promationinfo,27349500555691_33985315097099_0_promationinfo,27117783705678_39809454192655_0_promationinfo,25447770196802_16163885474822_0_promationinfo,26888670353597_39346507164695_0_promationinfo,25721436257845_38695747767061_0_promationinfo,26379333222078_39908890118674_0_promationinfo,26439985416618_40182167303440_0_promationinfo,27324448342727_20791607_0_promationinfo,26869610088909_32213062654471_0_promationinfo,26562847444665_32741159627271_0_promationinfo,25669618838573_38674479824397_0_promationinfo,25778279677887_23246336891655_0_promationinfo,26260790119095_38628563322647_0_promationinfo,25200891659721_16242652460039_0_promationinfo,26747703098319_16710008831238_0_promationinfo,20248019850120_42565397_0_promationinfo,5768727468934_24430555_0_promationinfo,17453382338824_16090042739719_0_promationinfo,1891476961153_28014907_0_promationinfo","dispCateName":"baojie"}';
        var s_ajax_param = 's_contact_baojie_196213900193485617909111756_';
        var s_ajax_param2 = 'sdfsdfsdfsdf';
    </script>

    """

    s_ajax_param_rule = r'var s_ajax_param = \'(\w+?)\';'
    s_ajax_param_compile = re.compile(s_ajax_param_rule, re.I)
    print s_ajax_param_compile.findall(test_str)

    ajax_param_rule = r'var ajax_param = \'(.*?)\';'
    ajax_param_compile = re.compile(ajax_param_rule, re.I)
    print ajax_param_compile.findall(test_str)
    print len(ajax_param_compile.findall(test_str)[0])


if __name__ == '__main__':
    test_01()
