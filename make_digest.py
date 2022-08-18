import requests
from blocks import DIGEST_HEADER, DIGEST_FOOTER
from utilities import formatted_url, itemize

# Where's the list of articles to include in each section?
DIGEST_IN = "digest-in.txt"

# Where should the code be output?
DIGEST_OUT = "digest-out.txt"

# User-agent data for request (necessary to not be blocked by our web host)
# This was set as a custom allowed rule by WP Engine support just for us
USER_AGENT = {"User-agent": "9Ds8MnNbYcg5t376c8m6"}
ENDPOINT = "https://stanforddaily.com/wp-json/wp/v2/posts"
SLUG_MAP = {
    "THE GRIND": "thegrind",
    "DATA": "94305",
    "ARTS & LIFE": "arts-life"
}
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
    def __init__(self, url, headline, image_url, subtitle, authors, excerpt, featured=False):
        self.url = url
        self.headline = headline
        self.image_url = image_url
        self.subtitle = subtitle
        self.authors = authors
        self.excerpt = excerpt
        self.featured = featured

    def byline(self):
        return itemize(self.authors)

    @classmethod
    def from_json(cls, data, featured=False):
        return cls(
            formatted_url(data["link"]),
            data["title"]["rendered"],
            data["jetpack_featured_media_url"],
            data["wps_subtitle"],
            data["parsely"]["meta"]["creator"],
            data["excerpt"]["rendered"],
            featured=featured
        )

    def render(self):
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

            feature_image = f"""
                    <tr>
                        <td align="center" valign="top" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;">
                            <a href="{formatted_url(self.url)}" style="text-decoration: none;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" target="_blank">
                            <img border="0" class="em_full_img" height="300" src="{self.image_url}" style="display: block;font-family: Arial, sans-serif;font-size: 20px;line-height: 25px;color: #424242;max-width: 520px;border: 0 !important;height: auto;outline: none !important;text-decoration: none;-ms-interpolation-mode: bicubic;" width="540">
                        </a>
                        </td>
                    </tr>
                    """
            feature_image += str(Spacer(25))
        else:
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
                By {self.byline()}   ●
               </span>
               <a href="{formatted_url(self.url)}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;color: inherit !important;text-decoration: none !important;">
                <span style="font-family: 'Open Sans', Arial, sans-serif;font-size: 12px;line-height: 15px;color: #8c1514;font-weight: bold;margin-bottom: 5px;border-collapse: collapse;mso-line-height-rule: exactly;">
                 READ MORE »
                </span>
               </a>
              </td>
             </tr>
        """

        return feature_image + headline + excerpt + byline


class Section:
    def __init__(self, urls, name=None, featured=False):
        self.name = name
        slugs = [x.split('/')[6] for x in urls]
        response = requests.get(ENDPOINT, params={"slug": ','.join(slugs)})
        data = response.json()
        self.articles = [Article.from_json(item, featured=featured) for item in data]

    def render(self):
        if self.name is None or "CARTOON" in self.name:
            title = ""
        else:
            title = f"""
                    <tr><td align="left" class="em_defaultlink" style="font-family: 'Open Sans', Arial, sans-serif;font-size: 17px;line-height: 21px;color: #8c1514;font-weight: 900;padding-bottom: 5px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;" valign="top">
                      <a href="{formatted_url(CATEGORY_PAGES[self.name])}" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;border-collapse: collapse;color: inherit !important;text-decoration: none !important;">
                       {self.name.upper()}
                      </a>
                     </td>
                     </tr>
                    """

        return title + Spacer.small() + Spacer.large().join(x.render() for x in self.articles)


def write_digest(digest):
    print(f"Writing to {DIGEST_OUT}...")
    # TODO: - Prettify like before.
    with open(DIGEST_OUT, "w") as o:
        # o.write(BeautifulSoup(digest, "html.parser").prettify())
        o.write(digest)


def sections_from_file(directory):
    with open(directory) as file:
        lines = [x for x in map(lambda r: r.strip(), file.readlines()) if len(x) > 0]
    indices = [i for i, x in enumerate(lines) if x in ALL_SECTIONS]
    sections_in = []
    for i in range(0, len(indices) - 1):
        section_name = lines[indices[i]]
        group = lines[indices[i]:indices[i + 1]]
        sections_in.append(Section(group[1:], name=section_name, featured=section_name.lower() == "featured"))

    return sections_in


if __name__ == "__main__":
    sections = sections_from_file(DIGEST_IN)
    digest_out = DIGEST_HEADER + (Spacer.large() + Divider.default()).join(x.render() for x in sections)
    digest_out += Spacer.large() + DIGEST_FOOTER
    write_digest(digest_out)
