import requests
from blocks import DIGEST_HEADER, DIGEST_FOOTER, DIGEST_AD, SPORTS_BANNER
from utilities import formatted_url, itemize
from bs4 import BeautifulSoup
import re

# Where's the list of articles to include in each section?
DIGEST_IN = "digest-in.txt"

# Where should the code be output?
DIGEST_OUT = "digest-out.html"

# User-agent data for request (necessary not to be blocked by our web host) is written below.
# This was set as a custom allowed rule by WP Engine support just for us.

USER_AGENT = {"User-agent": "9Ds8MnNbYcg5t376c8m6"}
ENDPOINT = "https://stanforddaily.com/wp-json/wp/v2/posts"
CATEGORY_PAGES = {
    "FEATURED": "",
    "NEWS": "https://stanforddaily.com/category/news/",
    "OPINIONS": "https://stanforddaily.com/category/opinions/",
    "SPORTS": "https://stanforddaily.com/category/sports/",
    "ARTS & LIFE": "https://stanforddaily.com/category/arts-life/",
    "THE GRIND": "https://stanforddaily.com/category/thegrind/",
    "HUMOR": "https://stanforddaily.com/category/humor/",
    "DATA": "https://stanforddaily.com/category/@94305/",
    "PODCASTS": "https://stanforddaily.com/category/podcasts/",
    "VIDEO": "https://www.youtube.com/channel/UCWg3QqUzqxXt6herm5sMjNw",
    "CARTOON OF THE WEEK": "https://stanforddaily.com/category/cartoons/",
    "CARTOON OF THE DAY": "https://stanforddaily.com/category/cartoons/",
    "CARTOONS": "https://stanforddaily.com/category/cartoons/"
}
ALL_SECTIONS = list(CATEGORY_PAGES.keys())


class Spacer:
    def __init__(self, height):
        self.height = height  # px

    def __str__(self):
        return f"""
                <tr>
                    <td class="em_height" height="{self.height}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
                    </td>
                </tr>
            """

    @classmethod
    def small(cls):
        return str(cls(10))

    @classmethod
    def large(cls):
        return str(cls(25))


class Divider:
    def __init__(self, height):
        self.height = height  # px

    def __str__(self):
        return f"""
            <tr>
                <td align="center" style="font-size: 0px;line-height: 0px;height: {self.height}px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" valign="top">
                    <hr>
                </td>
            </tr>
        """

    @classmethod
    def default(cls):
        return str(cls(3))


class Article:
    def __init__(self, url, headline, image_url, subtitle, authors, excerpt, content, featured=False, cartoon=False):
        self.url = url
        self.headline = headline
        self.image_url = image_url
        self.subtitle = subtitle
        self.authors = authors
        self.excerpt = excerpt
        self.content = content
        self.featured = featured
        self.cartoon = cartoon

    def byline(self):
        return itemize(self.authors)

    @classmethod
    def from_json(cls, data, featured=False):
        cartoon = 41527 in data["categories"]
        return cls(
            formatted_url(data["link"]),
            data["title"]["rendered"],
            data["jetpack_featured_media_url"],
            data["wps_subtitle"],
            data["parsely"]["meta"]["creator"],
            data["excerpt"]["rendered"],
            data["content"]["rendered"],
            featured=featured,
            cartoon=cartoon
        )

    def render(self):
        headline = f"""
                        <tr>
                            <td align="left" class="em_defaultlink" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 17px;line-height: 21px;color: #000000;font-weight: 900;padding-bottom: 12px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" valign="top">
                                <a href="{formatted_url(self.url)}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;color: inherit !important;text-decoration: none !important;">
                                {self.headline}
                                </a>
                            </td>
                        </tr>
                    """

        feature_image = ""
        if self.featured:
            headline = f"""
                        <tr>
                            <td align="left" class="em_defaultlink" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 25.5px;line-height: 31.5px;color: #000000;font-weight: bold;padding-bottom: 12px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" valign="top">
                                <a href="{formatted_url(self.url)}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;color: inherit !important;text-decoration: none !important;">
                                    {self.headline}
                                </a>
                            </td>
                        </tr>
                    """
        if self.featured or self.cartoon:
            feature_image = f"""
                            <tr>
                                <td align="center" valign="top" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
                                    <a href="{formatted_url(self.url)}" style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" target="_blank">
                                    <img border="0" class="em_full_img" height="300" src="{self.image_url}" style="display: block;font-family: Arial, sans-serif;font-size: 20px;line-height: 25px;color: #424242;max-width: 520px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" width="540">
                                </a>
                                </td>
                            </tr>
                        """
            feature_image += Spacer.large()

        excerpt = f"""
                    <tr>
                        <td align="left" class="article-excerpt em_gray" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 14px;line-height: 20px;color: #5b5b5b;padding-bottom: 12px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" valign="top">
                            {self.excerpt}
                        </td>
                    </tr>
                """

        byline = f"""
                <tr>
                    <td align="left" class="em_defaultlink" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 14px;line-height: 14px;color: #5b5b5b;font-weight: 900;padding-bottom: 12px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" valign="top">
                       <span style="font-weight: bold;color: #5b5b5b;border-collapse: collapse;mso-line-height-rule: exactly;">
                        By {self.byline()}   \u25CF</span>
                        <a href="{formatted_url(self.url)}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;color: inherit !important;text-decoration: none !important;">
                            <span style="font-family: 'Open Sans', Arial, sans-serif;font-size: 12px;line-height: 15px;color: #8c1514;font-weight: bold;margin-bottom: 5px;border-collapse: collapse;mso-line-height-rule: exactly;">
                                 READ MORE »
                            </span>
                        </a>
                    </td>
                </tr>
            """

        return feature_image + headline + excerpt + byline

    def render_content(self):
        soup = BeautifulSoup(self.content, "html.parser")
        bold = soup.find_all(lambda t: re.search(r"(^.*ball)", t.text.lower()) is not None)
        for match in bold:
            match.string.wrap(soup.new_tag("strong"))
        # print(bold)
        # print(re.search(r"(golf)", soup.text.lower()).groups())
        print(bold)
        pre = r"<figure.*?>(.+?)</figure>"
        print([x["src"] for x in soup.findAll("img") if x.has_attr("src") and "stanforddaily.com" in x["src"]])
        img_example = """
        <a href="https://stanforddaily.com/category/sports/" target="_blank" style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;"><img class="em_full_img" src="https://stanforddaily.com/wp-content/uploads/2022/04/sports-graphic.png" width="532.8" height="355.2" border="0" style="display: block;font-family: Arial, sans-serif;font-size: 20px;line-height: 25px;color: #424242;max-width: 520px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;"></a>
        """

        out = f"""
                            <tr>
                                <td align="left" class="article-excerpt em_gray" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 14px;line-height: 20px;color: #5b5b5b;padding-bottom: 12px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" valign="top">
                                    {re.sub(pre, img_example, self.content)}
                                </td>
                            </tr>
                        """
        return re.sub(r"<p.*?>.*?(volleyball)", "<p><strong>volleyball</strong>", out)


class Section:
    def __init__(self, urls, name=None, featured=False):
        self.name = name
        slugs = [x.split('/')[6] for x in urls]
        response = requests.get(ENDPOINT, params={"slug": ','.join(slugs)})
        data = response.json()

        # Accounts for any ordering that may have been lost, as the response comes back as a dictionary, not an array.
        sorting = {slug: index for index, slug in enumerate(slugs)}
        try:
            self.articles = [Article.from_json(item, featured=featured) for item in sorted(data, key=lambda s: sorting[s["slug"]])]
        except KeyError:
            self.articles = [Article.from_json(item, featured=featured) for item in data]
        self.featured = featured

    def render(self):
        if self.name is None or "CARTOON" in self.name or self.featured:
            title = ""
        else:
            title = f"""
                <tr>
                    <td align="left" class="em_defaultlink" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 17px;line-height: 21px;color: #8c1514;font-weight: 900;padding-bottom: 5px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" valign="top">
                        <a href="{formatted_url(CATEGORY_PAGES[self.name])}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;color: inherit !important;text-decoration: none !important;">
                           {self.name.upper()}
                        </a>
                    </td>
                </tr>
            """

        return title + Spacer.small() + Spacer.large().join(x.render() for x in self.articles)


def write_digest(digest):
    print(f"Writing to {DIGEST_OUT}...")
    with open(DIGEST_OUT, "w", encoding="utf-8") as o:
        o.write(BeautifulSoup(str(digest), 'html.parser').prettify())


def sections_from_file(path):
    with open(path) as file:
        lines = [x for x in map(lambda r: r.strip(), file.readlines()) if len(x) > 0]

    section_names = [lines[0]]  # Add featured article(s) to the beginning.
    i = 1
    section_index = 0

    section_links = [[]]
    while lines[i] not in ALL_SECTIONS:
        section_links[section_index].append(lines[i])
        if i >= len(lines) - 1:
            break

        if lines[i + 1] in ALL_SECTIONS:
            section_names.append(lines[i + 1])
            section_links.append([])
            section_index += 1
            i += 1

        i += 1

    for index, group in enumerate(section_links):
        name = section_names[index]
        featured = name == "FEATURED"
        yield Section(group, name=name, featured=featured)


if __name__ == "__main__":
    sections = sections_from_file(DIGEST_IN)
    # digest_out = DIGEST_HEADER + (DIGEST_AD + Spacer.large() + Divider.default()).join(x.render() for x in sections)
    # digest_out += Spacer.large() + DIGEST_FOOTER
    this_week_section = Section(["https://stanforddaily.com/2022/09/18/this-week-in-sports-another-top-3-upset/"])
    this_week_article = this_week_section.articles[0]
    digest_out = DIGEST_HEADER + SPORTS_BANNER
    digest_out += this_week_article.render_content()
    digest_out += Spacer.large() + DIGEST_FOOTER
    write_digest(digest_out)
