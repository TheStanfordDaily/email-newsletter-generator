import sys
import requests
from make_digest import ENDPOINT, write_digest
from blocks import DIGEST_FOOTER, DIGEST_AD, MARKUP_HEADER


def markup_from_url(url):
    slug = url.split('/')[6]
    response = requests.get(ENDPOINT, params={"slug": slug, "_embed": "true"})
    data = response.json()[0]
    # TODO: Add URL query parameters to links in the content.
    # It works but does not look pretty. CSS needs to be updated or inserted here.
    feature_image = f"""
    <img style="width: 100%; height: 100%;" alt="A volleyball player jumps to serve the ball" class="wp-image-1211037" decoding="async" height="2081" loading="lazy" sizes="(max-width: 3121px) 100vw, 3121px" src="{data['jetpack_featured_media_url']}?w=800" srcset="{data['jetpack_featured_media_url']} 3121w, {data['jetpack_featured_media_url']}?resize=600,400 600w, {data['jetpack_featured_media_url']}?resize=768,512 768w, {data['jetpack_featured_media_url']}?resize=1200,800 1200w, {data['jetpack_featured_media_url']}?resize=1536,1024 1536w, {data['jetpack_featured_media_url']}?resize=2048,1366 2048w" width="3121">
     <em style="color: #5b5b5b;">
        {data["_embedded"]["wp:featuredmedia"][0]["caption"]["rendered"]}
     </em>
    """

    return "<h1>This Week in Sports</h1>" + data["content"]["rendered"]  # <h1>{data['title']['rendered']}</h1>


if __name__ == "__main__":
    markup = markup_from_url(sys.argv[1])  # ("https://stanforddaily.com/2022/10/23/this-week-in-sports-a-week-of-winning/")
    digest_out = MARKUP_HEADER + '<div class="elementor-widget-container">\n' + markup + '</div></body></html>'
    # write_digest(digest_out)
    with open("digest-out.html", "w") as f:
        f.write(digest_out)
