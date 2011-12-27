import unittest
from bors import Bors
from mock import Mock, sentinel
import re

teststr ="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html><head><title>SVT Text - 202 </title><meta http-equiv="Content-type" content="text/html; charset=iso-8859-1" /><meta http-equiv="Content-language" content="sv" /><meta name="Author" content="Sveriges Television AB, Stockholm, Sweden" /><meta name="Copyright" content="Sveriges Television AB, Stockholm, Sweden" /><meta name="Robots" content="index, follow, noarchive" /><meta name="Description" content="SVTs Text-TV p? internet. Nyheter, Ekonomi, Sport, M?lservice 377, V?der, TV... " /><link href="../../css/svttextstyle.css" rel="stylesheet" type="text/css" /><link href="../locals/localstyle.css" rel="stylesheet" type="text/css" /><script language="JavaScript" type="text/javascript"><!--var nextPage = "201.html";var previousPage = "203.html";// --></script><script language="JavaScript" src="../../script/svttextscript.js" type="text/javascript"></script><script language="JavaScript" src="../locals/localscript.js" type="text/javascript"></script></head><body onload="setFocus('navform','pageinput');" bgcolor="#FFFFFF"><a name="AnchorTop"></a><div id="logo"><a href="100.html"><img src="../../images/logoSvtText.gif" width="146" height="26" alt="SVT Text" border="0" /></a></div><div id="wrapper"><div id="topLine"></div><ul id="menu"><li><span class="mpNumber"><a href="100.html" class="mpNumber"> 100</a></span><a href="100.html">Nyheter</a></li><li><span class="mpNumber"><a href="200.html" class="mpNumber"> 200</a></span><a href="200.html">Ekonomi</a></li><li><span class="mpNumber"><a href="300.html" class="mpNumber"> 300</a></span><a href="300.html">Sport</a></li><li><span class="mpNumber"><a href="400.html" class="mpNumber"> 400</a></span><a href="400.html">V?der</a></li><li><span class="mpNumber"><a href="500.html" class="mpNumber"> 500</a></span><a href="500.html">Blandat</a></li><li><span class="mpNumber"><a href="600.html" class="mpNumber"> 600</a></span><a href="600.html">P? TV</a></li><li><span class="mpNumber"><a href="700.html" class="mpNumber"> 700</a></span><a href="700.html">Inneh?ll</a></li><li><span class="mpNumber"><a href="800.html" class="mpNumber"> 800</a></span><a href="800.html">UR</a></li><li id="help"><a href="javascript:SgOpenArgs('http://svt.se/svt/jsp/Crosslink.jsp?d=50238','texttvhelp','550','500','status=yes,scrollbars=yes');">Hj&auml;lp</a> <img src="../../images/iconHelp.gif" width="13" height="13" alt="" border="0" align="middle" /></li></ul><div id="topNav"><span class="leftSetting">Utseende: <a href="javascript:settingsNavigate(webLookFolder,202);" class="webView" title="Visa sidan med webbutseende">Webb</a> | <a href="javascript:settingsNavigate(tvLookFolder,202);" class="tvView" title="Visa sidan med TV-utseende">TV</a></span><div class="centerNav"><form title="Navigering till sidnummer" id="navform" name="navform" action="jsp/gotopage.jsp" onsubmit="return formNavigate(this);"><a href="201.html" class="btnBg"><img onmouseover="effect(this);" onmouseout="noEffect(this)" src="../../images/btnBack.gif" width="31" height="18" alt="F?reg?ende sida" border="0" /></a>&nbsp;<input id="pageinput" name="pageinput" type="text" maxlength="3"  title="Ange ?nskat sidnummer" value="202" />&nbsp;<span class="btnBg"><input id="submitButton" onmouseover="effect(this);" onmouseout="noEffect(this)" type="image" src="../../images/btnGoToPage.gif" title="G? till sida" value="G? till sida" alt="G? till sida" /></span>&nbsp;<a href="203.html" class="btnBg"><img onmouseover="effect(this);" onmouseout="noEffect(this)" src="../../images/btnForward.gif" width="31" height="18" alt="N?sta sida" border="0" /></a></form></div><span class="sizeSetting"><a href="javascript:settingsNavigate(normalSizeFolder,202);" class="aNormal">normal</a> | <a href="javascript:settingsNavigate(largeSizeFolder,202);" class="aLarger">st?rre</a> | <a href="javascript:settingsNavigate(xlargeSizeFolder,202);" class="aLargest">st?rst</a></span></div><?xml version="1.0" encoding="UTF-8" standalone="no"?><div><a class="preclass" name="subpage1"> </a><pre class="root"> 202 SVT Text         M?ndag 04 jul 2011
 K?lla: SIX Telekurs                    
 <span class="Y bgY DH"> </span><span class="Y bgY DH"> </span><span class="Y bgY DH"> </span><span class="R bgY DH">B?RSEN            KL 15.30   4/7    </span>
 <span class="Y"> OMS?TTNING LARGE CAP mkr  4984 (11799)</span>
 <span class="Y"> H?jda  63  ( 44)   </span><span class="C"> S?nkta  11   ( 31)</span>
 <span class="W"> Oms. Stockholmsb?rsen     5296 (12383)</span>
 <span class="W">  (parentes = f?reg?ende b?rsdags slut)</span>
 <span class="G">                                       </span>
 <span class="C DH"> </span><span class="C DH">OMX STOCKHOLM (17:04)   303.55  -0.51 </span>
 <span class="Y"> ENERGI                 1329.05  +1.63 </span>
 <span class="Y"> MATERIAL                266.73  +1.20 </span>
 <span class="Y"> INDUSTRIVAROR           471.82  +0.93 </span>
 <span class="Y"> S?LLANK?PSVAROR         843.25  +1.21 </span>
 <span class="Y"> DAGLIGVAROR             599.64  +1.38 </span>
 <span class="Y"> H?LSOV?RD               274.13  +0.99 </span>
 <span class="Y"> FINANS &amp; FASTIGHET      419.20  +0.39 </span>
 <span class="Y"> INFORMATIONSTEKNIK      185.28  +0.35 </span>
 <span class="Y"> TELEKOMOPERAT?RER       754.84  +0.27 </span>
 <span class="C"> KRAFTF?RS?RJNING        157.39  -0.25 </span>
 <span class="W">                                       </span>
 <span class="W">                                       </span>
 <span class="Y bgY"> </span><span class="Y bgY">       </span><span class="R bgY">Index 100 = 31/12 1995         </span>
</pre></div><div class="subWrapper"><div class="subArea"></div></div><div class="clear" id="footerWrapper"><div id="bottomNav"><span class="leftSetting">Automatisk uppdatering: <a href="javascript:settingsNavigate(updateOffFolder,202);" class="updateOff">Av</a> | <a href="javascript:settingsNavigate(updateOnFolder,202);" class="updateOn">P?</a></span><div class="centerNav"><a href="201.html" class="btnBg"><img onmouseover="effect(this);" onmouseout="noEffect(this)" src="../../images/btnBack.gif" width="31" height="18" alt="F?reg?ende sida" border="0" /></a>&nbsp;<span class="upArrow"><a href="#AnchorTop" class="btnBg"><img onmouseover="effect(this);" onmouseout="noEffect(this)" src="../../images/btnUp.gif" width="19" height="18" alt="" border="0" /></a></span>&nbsp;<a href="203.html" class="btnBg"><img onmouseover="effect(this);" onmouseout="noEffect(this)" src="../../images/btnForward.gif" width="31" height="18" alt="N?sta sida" border="0" /></a></div></div></div></div><div class="clear subWrapper"><div class="copyArea"><p>&copy; Sveriges Television AB | Mikael Hvinlund |  <a href="mailto:text@svt.se">text@svt.se</a></p></div></div><!-- Begin Sitestat code --><script language=JavaScript1.1 type=text/javascript>sitestat("http://ld.svt.se/svt/svt/s?svt-text.Ekonomi.202&client=svttext");</script><noscript><img src="http://ld.svt.se/svt/svt/s?svt-text.Ekonomi.202&client=svttext" width="1" height="1" alt=""></noscript><!-- End Sitestat code --></body></html>"""

class MockBorsTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def checkMatch(self, match):
           if match is None:
               return False

           return True

    def testgetIndex(self):

       bors = Bors()

       #put the monkey patch in place
       bors.get_texttv = Mock()
       bors.get_texttv.return_value = teststr

       # fire away
       result = bors.getindex()

       self.assertTrue(bors.get_texttv.called)
       self.assertTrue(type(result), type(' '))

       # a better check of the result
       self.valid = re.compile(r'\d{3}\.\d{2}')  # eg 357.57
       self.assertTrue(self.checkMatch(self.valid.match(result)))

    def testgetdeviation(self):

       bors = Bors()

       #put the monkey patch in place
       bors.get_texttv = Mock()
       bors.get_texttv.return_value = teststr

       # fire away
       result = bors.getdeviation()

#       print result

       self.assertTrue(bors.get_texttv.called)
       self.assertTrue(type(result), type(' '))
       self.valid = re.compile(r'[-+]\d{1,2}\.\d{1,2}')  # eg +/-0.79
       self.assertTrue(self.checkMatch(self.valid.match(result)))

if __name__ == '__main__':
    unittest.main()
