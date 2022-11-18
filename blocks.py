from datetime import date
from utilities import formatted_url

# Header HTML in each digest
DIGEST_HEADER = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <!--[if gte mso 9]>
    <xml>
      <o:OfficeDocumentSettings>
        <o:AllowPNG />
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    <!--[if !mso]><!-->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i" rel="stylesheet" type="text/css">
    <!--<![endif]-->
    <style type="text/css">
        #the_title {
            padding-left: 10px;
        }
        #featured_fields1 {
            padding: 10px;
            margin: 10px;
            border-style: solid;
            border-color: #8c1514;
            border-radius: 25px;
            background-color: lightcyan;
        }
        #featured_fields2 {
            padding: 10px;
            margin: 10px;
            border-style: solid;
            border-color: #8c1514;
            border-radius: 25px;
            background-color: lightpink;
        }
        #featured_fields3 {
            padding: 10px;
            margin: 10px;
            border-style: solid;
            border-color: #8c1514;
            border-radius: 25px;
            background-color: lightyellow;
        }
        textarea {
        width: 100%;
        height: 2vh;
        }
        #Mailchimp_output {
            width: 100%;
            height: 50vh;
        }
      body {
        margin:0 !important;
        padding:0 !important;
        -webkit-text-size-adjust:100% !important;
        -ms-text-size-adjust:100% !important;
        -webkit-font-smoothing:antialiased !important;
      }
      img {
        border:0 !important;
        outline:none !important;
      }
      p {
        margin:0 !important;
        padding:0 !important;
      }
      table {
        border-collapse:collapse;
        mso-table-lspace:0;
        mso-table-rspace:0;
      }
      td,a,span {
        border-collapse:collapse;
        mso-line-height-rule:exactly;
      }
      .ExternalClass * {
        line-height:100%;
      }
      .em_defaultlink a {
        color:inherit !important;
        text-decoration:none !important;
      }
      span.MsoHyperlink {
        mso-style-priority:99;
        color:inherit;
      }
      span.MsoHyperlinkFollowed {
        mso-style-priority:99;
        color:inherit;
      }
      .tpl-content {
        padding:0 !important;
      }
      .em_white a {
        color:#ffffff;
        text-decoration:none;
      }
      .em_black a {
        color:#000000;
        text-decoration:none;
      }
      .em_gray a {
        color:#969696;
        text-decoration:none;
      }
      @media only screen and (min-width:481px) and (max-width:619px) {
        .em_main_table {
          width:480px !important;
        }
        .em_wrapper {
          width:100% !important;
        }
        .em_spacer {
          width:20px !important;
        }
        .em_hide {
          display:none !important;
        }
        .em_full_img {
          width:100% !important;
          height:auto !important;
          max-width:none !important;
        }
        .em_center {
          text-align:center !important;
        }
        .em_height {
          height:20px !important;
        }
        .em_pad_top {
          padding-top:20px !important;
        }
        .em_aside {
          padding:0 20px !important;
        }
        .em_br {
          display:block !important;
        }
        .em_auto {
          height:auto !important;
        }
        .em_bg {
          background-color:#ff1061 !important;
          background-image:none !important;
        }
        .em_bg1 {
          background-color:#ffffff !important;
        }
      }
      @media only screen and (min-width:375px) and (max-width:480px) {
        .em_main_table {
          width:375px !important;
        }
        .em_wrapper {
          width:100% !important;
        }
        .em_spacer {
          width:15px !important;
        }
        .em_hide {
          display:none !important;
        }
        .em_full_img {
          width:100% !important;
          height:auto !important;
          max-width:none !important;
        }
        .em_center {
          text-align:center !important;
        }
        .em_height {
          height:20px !important;
        }
        .em_pad_top {
          padding-top:20px !important;
        }
        .em_aside {
          padding:0 15px !important;
        }
        u + .em_body .em_full_wrap {
          width:100% !important;
          width:100vw !important;
        }
        .em_br {
          display:block !important;
        }
        .em_auto {
          height:auto !important;
        }
        .em_bg {
          background-color:#ff1061 !important;
          background-image:none !important;
        }
        .em_bg1 {
          background-color:#ffffff !important;
        }
      }
      @media screen and (max-width:374px) {
        .em_main_table {
          width:320px !important;
        }
        .em_wrapper {
          width:100% !important;
        }
        .em_spacer {
          width:15px !important;
        }
        .em_hide {
          display:none !important;
        }
        .em_full_img {
          width:100% !important;
          height:auto !important;
          max-width:none !important;
        }
        .em_center {
          text-align:center !important;
        }
        .em_height {
          height:20px !important;
        }
        .em_pad_top {
          padding-top:20px !important;
        }
        .em_aside {
          padding:0 15px !important;
        }
        u + .em_body .em_full_wrap {
          width:100% !important;
          width:100vw !important;
        }
        .em_br {
          display:block !important;
        }
        .em_auto {
          height:auto !important;
        }
        .em_bg {
          background-color:#ff1061 !important;
          background-image:none !important;
        }
        .em_bg1 {
          background-color:#ffffff !important;
        }
        .em_line {
          background-image:url(images/dot_image.jpg) !important;
          height:3px !important;
        }
      }

      .top_prompts a {
         font-size: 1rem;
      }

      @media screen and (max-width:640px) {
         .top_prompts a {
             font-size: 0.75em;
         }
      }""" + f"""
    </style>
      <body style="height: 100%;margin: 0 !important;padding: 0 !important;width: 100%;-ms-text-size-adjust: 100% !important;-webkit-text-size-adjust: 100% !important;background-color: #FAFAFA;-webkit-font-smoothing: antialiased !important;">
        <center>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="em_full_wrap" bgcolor="#ffffff">
      <tbody><tr>
        <td align="center" valign="top">
          <table align="center" width="620" border="0" cellspacing="0" cellpadding="0" class="em_main_table" style="width:620px;">
            <!--Pre_Header-->
            <tbody><tr>
              <td align="center" valign="top" bgcolor="#303030" class="em_aside" style="padding:0 30px;">
                <table align="center" width="560" border="0" cellspacing="0" cellpadding="0" class="em_wrapper" style="width:560px;">
                  <tbody><tr>
                    <td valign="top" align="center">
                      <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                        <tbody><tr>
                          <td valign="top" align="center">
                            <table width="275" border="0" cellspacing="0" cellpadding="0" align="left" class="em_wrapper">
                              <tbody><tr>
                                <td height="20" style="font-size:1px;line-height:1px;">&nbsp;</td>
                              </tr>
                            </tbody></table>
                            <!--[if gte mso 9]>
                          </td>
                          <td valign="top">
                            <![endif]-->
                            <table width="275" border="0" cellspacing="0" cellpadding="0" align="right" class="em_wrapper">
                              <tbody><tr>
                                <td align="right" valign="top" class="em_defaultlink em_center" mc:edit="pre2" style="font-family:'Open Sans', Arial, sans-serif;font-size:10px;line-height:11px;color:#ffffff;">
                                  <a href="{formatted_url("https://www.stanforddaily.com/")}">stanforddaily.com | {date.today().strftime("%B %d, %Y")}</a>
                                </td>
                              </tr>
                              <tr>
                                <td height="35" class="em_height">&nbsp;</td>
                              </tr>
                              <tr>
                                <td align="right" valign="top" class="em_defaultlink em_center" mc:edit="pre2" style="font-family:'Open Sans', Arial, sans-serif;font-size:10px;line-height:11px;color:#ffffff;">
                                  <a href="*|ARCHIVE|*" target="_blank" style="text-decoration:none;color:#7d7d7d;">Click to view this email in your browser</a>
                                </td>
                              </tr>
                            </tbody></table>
                          </td>
                        </tr>
                      </tbody></table>
                    </td>
                  </tr>
                  <tr>
                    <td height="16" style="font-size:1px;line-height:1px;">&nbsp;</td>
                  </tr>
                </tbody></table>
              </td>
            </tr>
            <!--//Pre_Header-->
            <!--Header-->
            <!--//Module 5-->
          </tbody></table>
        </td>
      </tr>
      <tr>
        <td align="center" valign="top">
          <table align="center" width="620" border="0" cellspacing="0" cellpadding="0" class="em_main_table" style="width:620px;">
            <!--Module 6-->
            <tbody><tr>
              <td align="center" valign="top" style="padding:0 50px;" class="em_aside">
                <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
		<!-- AD
                  <tr>
                    <td height="30" class="em_height"> </td>
                 </tr>
		<tr>
                    <td align="center" valign="top">
                      <a href="WEBLINK" target="_blank" style="text-decoration:none;"><img mc:edit="image6" class="em_full_img" src="IMAGELINK" width="1050" height="170" alt="IMAGEALT" border="0" style="display:block;font-family:Arial, sans-serif; font-size:20px; line-height:25px; color:#424242; max-width:520px; max-height:59.5px;"></a>
                    </td>
                  </tr>
		-->
        <tbody>
            <tr>
                <td height="30" class="em_height">&nbsp;</td>
            </tr>
            <tr>
            <td align="center" valign="top">
              <a href="{formatted_url("https://www.stanforddaily.com/")}" target="_blank" style="text-decoration:none;"><img mc:edit="image6" class="em_full_img" src="https://wp.stanforddaily.com/wp-content/uploads/2019/11/cropped-DailyLogo-CardinalRed.png" width="600" height="180" alt="The Stanford Daily logo" border="0" style="display:block;font-family:Arial, sans-serif; font-size:20px; line-height:25px; color:#424242; max-width:520px; max-height:59.5px;"></a>
            </td>
            </tr>
		    <tr>
            <td>
              <div class="top_prompts" style="display: flex;margin-top: 10px;"><a class="top_prompts" href="{formatted_url("https://www.stanforddaily.com/tips/")}" style="margin-left:auto;margin-right:10px;font-family:'Open Sans', Arial, sans-serif;font-weight: bold;color:#8c1514; text-decoration: none; border-right: 3px solid #8c1514;padding-right:10px;">SUBMIT A TIP</a><a class="top_prompts" href="{formatted_url("https://www.stanforddaily.com/donate/")}" style="font-family:'Open Sans', Arial, sans-serif;font-weight: bold;color:#8c1514; text-decoration: none;">DONATE</a><a class="top_prompts" href="{formatted_url("https://www.stanforddaily.com/submitting-to-the-daily/")}" style="margin-right:auto;border-left: 3px solid #8c1514; margin-left:10px;padding-left:10px;font-family:'Open Sans', Arial, sans-serif;font-weight: bold;color:#8c1514; text-decoration: none;">SUBMIT WORK</a></div>
            </td>
            </tr>
            <tr>
                <td height="30" style="font-size:1px;line-height:1px;">&nbsp;</td>
            </tr>
        <!-- AD
        <tr>
          <td style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse; padding-bottom: 25px;">
            <a href=WEBLINK style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" target="_blank">
              <img alt="" border="0" class="em_full_img" height="180" src=IMAGELINK style="display: block;font-family: Arial, sans-serif;font-size: 20px;line-height: 25px;color: #424242;max-width: 520px;max-height: 59.5px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" width="600">
            </a>
          </td>
        </tr>
        -->
"""

# Footer HTML used in each digest
DIGEST_FOOTER = f"""
        <!-- AD
          <tr>
            <td style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse; padding-bottom: 25px;">
              <a href=WEBLINK style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" target="_blank">
                <img alt="" border="0" class="em_full_img" height="180" src=IMAGELINK style="display: block;font-family: Arial, sans-serif;font-size: 20px;line-height: 25px;color: #424242;max-width: 520px;max-height: 59.5px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" width="600">
              </a>
            </td>
           </tr>
          -->
</tbody></table>
</td>
</tr>
</tbody></table>
</td>
</tr>
<!--//Module 6-->
</tbody></table>
<!--//This one-->
<table align="center" width="620" border="0" cellspacing="0" cellpadding="0" class="em_main_table" style="width: 620px;border-collapse: collapse;mso-table-lspace: 0;mso-table-rspace: 0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
<!--Footer-->
<tbody><tr>
<td align="center" valign="top" bgcolor="#8c1514" style="padding: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" class="em_aside">
<table align="center" width="560" border="0" cellspacing="0" cellpadding="0" class="em_wrapper" style="width: 560px;border-collapse: collapse;mso-table-lspace: 0;mso-table-rspace: 0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
<tbody><tr>
<td height="5" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
</tr>
<!--//Footer-->
<tr>
<td align="center" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<a href="{formatted_url("https://www.stanforddaily.com/tips/")}" class="em_defaultlink" style="text-decoration: none;font-family: 'Open Sans', Arial, sans-serif;font-size: 18px;line-height: 24px;color: #ffffff;font-weight: 900;padding-bottom: 12px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">Are we missing something? Click here to send us a tip.</a>
</td>
</tr>
<tr>
<td height="5" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
</tr>
</tbody></table>
<!--End of this one-->
<!--Footer-->
</td>
</tr>
<tr>
<td align="center" valign="top" bgcolor="#303030" style="padding: 0 3px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" class="em_aside">
<table align="center" width="560" border="0" cellspacing="0" cellpadding="0" class="em_wrapper" style="width: 560px;border-collapse: collapse;mso-table-lspace: 0;mso-table-rspace: 0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
<tbody><tr>
<td valign="top" align="center" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<table width="190" border="0" cellspacing="0" cellpadding="0" align="left" class="em_wrapper" style="width: 190px;border-collapse: collapse;mso-table-lspace: 0;mso-table-rspace: 0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
<tbody><tr>
<td height="30" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
</tr>
<tr>
<td align="left" valign="top" class="em_white em_center" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 10px;line-height: 15px;color: #ffffff;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<span style="font-weight: bold;color: #ffffff;border-collapse: collapse;mso-line-height-rule: exactly;"><a href="{formatted_url("https://www.stanforddaily.com/join")}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;color: #ffffff;text-decoration: none;">Click Here to Join Our Staff</a></span>
<br>
<br>
<span style="font-weight: bold;color: #ffffff;border-collapse: collapse;mso-line-height-rule: exactly;"><a href="{formatted_url("https://www.stanforddaily.com/about")}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;color: #ffffff;text-decoration: none;">Contact Us</a></span>
<br>
<br>
456 Panama Mall, Stanford CA, 94305
<a href="mailto:eic@stanforddaily.com" style="text-decoration: none;color: #ffffff;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">| eic@stanforddaily.com</a>
</td>
</tr>
<tr>
<td height="47" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
</tr>
<tr>
<td align="left" valign="top" class="em_white em_center" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 12px;line-height: 15px;color: #ff1061;padding-bottom: 20px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<a href="{formatted_url("https://www.stanforddaily.com")}" target="_blank" style="text-decoration: none;color: #ffffff;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">www.stanforddaily.com</a>
</td>
</tr>
</tbody></table>
<!--[if gte mso 9]>
</td>
<td valign="top">
<![endif]-->
<table width="325" border="0" cellspacing="0" cellpadding="0" align="right" class="em_wrapper" style="width: 325px;border-collapse: collapse;mso-table-lspace: 0;mso-table-rspace: 0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
<tbody><tr>
<td height="35" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
</tr>
<tr>
<td valign="top" align="right" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<table border="0" cellspacing="0" cellpadding="0" align="right" class="em_wrapper" style="border-collapse: collapse;mso-table-lspace: 0;mso-table-rspace: 0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
<tbody><tr>
<td align="center" valign="top" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<table border="0" cellspacing="0" cellpadding="0" align="center" style="border-collapse: collapse;mso-table-lspace: 0;mso-table-rspace: 0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
<tbody><tr>
<td align="center" valign="top" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<a href="https://www.facebook.com/stanforddaily/" target="_blank" style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"><img src="https://wp.stanforddaily.com/wp-content/uploads/2019/11/wfb.png" width="27" height="27" alt="Facebook logo" style="display: block;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;color: #ffffff;font-weight: bold;max-width: 27px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" border="0"></a>
</td>
<td width="12" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
<td align="center" valign="middle" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<a href="https://www.instagram.com/stanforddaily/" target="_blank" style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"><img src="https://wp.stanforddaily.com/wp-content/uploads/2019/11/white_ig-e1573266355630.png" width="25" height="25" alt="Instagram logo" style="display: block;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;color: #ffffff;font-weight: bold;max-width: 30px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" border="0"></a>
</td>
<td width="8" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
<td align="center" valign="middle" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<a href="https://twitter.com/StanfordDaily" target="_blank" style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"><img src="https://wp.stanforddaily.com/wp-content/uploads/2019/11/wtwit.png" width="27" height="27" alt="Twitter logo" style="display: block;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;color: #ffffff;font-weight: bold;max-width: 27px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" border="0"></a>
</td>
<td width="11" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
<td align="center" valign="middle" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
<a href="https://www.youtube.com/user/TSDVideoMultimedia" target="_blank" style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"><img src="https://wp.stanforddaily.com/wp-content/uploads/2019/11/1280px-YouTube_light_icon_2017.svg_.png" width="27" height="19" alt="YouTube logo" style="display: block;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;color: #ffffff;font-weight: bold;max-width: 27px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" border="0"></a>
</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td height="105" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">&nbsp;</td>
</tr>
<tr>
<td align="right" valign="top" class="em_white em_center" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 10px;line-height: 15px;color: #ffffff;padding-bottom: 20px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">Don't want to receive these emails anymore? <a href="*|UNSUB|*" target="_blank" style="text-decoration: underline;color: #ffffff;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">Unsubscribe</a>
</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>
</td>
</tr>
<!--//Footer-->
<tr>
<td class="em_hide" style="line-height: 1px;min-width: 620px;background-color: #ffffff;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" bgcolor="#ffffff"><img alt="" src="https://gallery.mailchimp.com/a6e6e96fbb8fbb96fc6af9c6f/images/eaf2235c-906f-4e29-a5a7-0618ad4ffb7c.gif" height="1" width="620" style="max-height: 1px;min-height: 1px;display: block;width: 620px;min-width: 620px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" border="0">
</td>
</tr>
</tbody></table>
<div class="em_hide" style="white-space:nowrap;display:none;font-size:0px;line-height:0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div>
            </td>
        </tr>
    </tbody>
</table></td>
                            </tr>
                            <tr>
                                <td valign="top" id="templateHeader" style="background:#FFFFFF none no-repeat center/cover;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;background-color: #FFFFFF;background-image: none;background-repeat: no-repeat;background-position: center;background-size: cover;border-top: 0;border-bottom: 0;padding-top: 9px;padding-bottom: 0;"></td>
                            </tr>
                            <tr>
                                <td valign="top" id="templateBody" style="background:#FFFFFF none no-repeat center/cover;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;background-color: #FFFFFF;background-image: none;background-repeat: no-repeat;background-position: center;background-size: cover;border-top: 0;border-bottom: 2px solid #EAEAEA;padding-top: 0;padding-bottom: 9px;"></td>
                            </tr>
                            <tr>
                                <td valign="top" id="templateFooter" style="background:#FAFAFA none no-repeat center/cover;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;background-color: #FAFAFA;background-image: none;background-repeat: no-repeat;background-position: center;background-size: cover;border-top: 0;border-bottom: 0;padding-top: 9px;padding-bottom: 9px;">
                                
                        <!--[if (gte mso 9)|(IE)]>
                        </td>
                        </tr>
                        </table>
                        <![endif]-->
                        <!-- // END TEMPLATE -->
                    </td>
                </tr>
            </table>
        </center>
    </body>
</html>
"""

DIGEST_AD = """
<!-- AD
          <tr>
            <td style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse; padding-bottom: 25px;">
              <a href=WEBLINK style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" target="_blank">
                <img alt="" border="0" class="em_full_img" height="180" src=IMAGELINK style="display: block;font-family: Arial, sans-serif;font-size: 20px;line-height: 25px;color: #424242;max-width: 520px;max-height: 59.5px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" width="600">
              </a>
            </td>
           </tr>
          -->
        """

SPORTS_BANNER = """
                                <tr>
                                    <td height="10" style="font-size: 1px;line-height: 1px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"> </td>
                                </tr>
                                <tr>
                                    <td align="center" valign="top" style="width: 50%;font-size: 0px;line-height: 0px;height: 3px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
                                        <hr style="width:140px;color:#8c1514">
                                    </td>
                                </tr>
                                <tr>
                                    <td height="10" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"> </td>
                                </tr>
                                <tr>
                                    <td align="center" valign="top" class="em_defaultlink" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 40px;line-height: 45px;color: #615F5E;font-weight: 900;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
                                        <a style="color: #5019;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;text-decoration: none !important;" href="https://www.stanforddaily.com/category/sports/">This Week in Sports</a>
                                    </td>
                                </tr>
                                <!--<tr>
                    <td height="10" class="em_height"> </td>
                  </tr>
                  <tr>
                    <td align="center" valign="top">
                      <a href="https://www.stanforddaily.com/category/cartoons/" target="_blank" style="text-decoration:none;"><img mc:edit="image6" class="em_full_img" src="https://wp.stanforddaily.com/wp-content/uploads/2020/02/weekend_roundup_logo-1.jpg" width="200" height="200" alt="Weekend Roundup logo" border="0" style="display:block;font-family:Arial, sans-serif; font-size:20px; line-height:25px; color:#424242; max-width:200px;"></a>
                    </td>
                  </tr>-->
                                <tr>
                                    <td height="10" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"> </td>
                                </tr>
                                <tr>
                                    <td align="center" valign="top" style="width: 50%;font-size: 0px;line-height: 0px;height: 3px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
                                        <hr style="width:140px;color:#8c1514">
                                    </td>
                                </tr>
                                <tr>
                                    <td height="10" class="em_height" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"> </td>
                                </tr>
"""

MARKUP_HEADER = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700,700i" rel="stylesheet">
    <style>
        .elementor-widget-container {
            max-width: 600px;
            margin: auto;
        }
        figure > img {
            width: 100%;
            height: 100%;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        h1, p, li, figcaption {
            font-family: 'Open Sans';
        }
        a {
            color: #8c1514;
        }
    </style>
</head>
<body>
"""