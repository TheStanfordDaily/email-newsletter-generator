from bs4 import BeautifulSoup
from make_digest import Section

# Where's the list of articles to include in each section?
ROUNDUP_IN = "roundup-in.txt"

# Where should the code be output?
ROUNDUP_OUT = "roundup-out.txt"

TITLE = f"""
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
"""


def article_from_file(path):
    with open(path) as file:
        lines = [x for x in map(lambda r: r.strip(), file.readlines()) if len(x) > 0]
    if len(lines) > 0:
        return Section(lines)


introduction = f"""
    <tr>
        <td align="center" valign="top" class="em_defaultlink" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 16px;line-height: 20px;color: black;font-weight: 500;padding-bottom: 5px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
    Welcome to This Week In Sports. We are The Daily’s sports editors, Sofia Scekic and Gavin McDonell, and we’ll be walking you through the major games, events and stories from the past week, as well as providing a brief preview of what’s coming up this week.
        </td>
    </tr>
"""


def markup_from_content(article):
    elements = BeautifulSoup(article.content, "html.parser").find_all(["p", "img"])
    for element in elements:
        if element.name == 'p':
            element["style"] = "max-width: 100%;"
    return '\n'.join(map(str, elements))


def write_roundup(roundup):
    print(f"Writing to {ROUNDUP_OUT}...")
    with open(ROUNDUP_OUT, "w") as o:
        o.write(BeautifulSoup(roundup, "html.parser").prettify())


if __name__ == "__main__":
    first_article = article_from_file(ROUNDUP_IN).articles[0]  # grabs first one by default
    markup = markup_from_content(first_article)
    # roundup_out = ROUNDUP_HEADER + markup
    # roundup_out += Spacer.large() + DIGEST_FOOTER
    # write_roundup(roundup_out)
    print(markup)