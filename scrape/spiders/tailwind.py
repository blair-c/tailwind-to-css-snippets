import scrapy


class TailwindSpider(scrapy.Spider):
    name = "tailwind"
    allowed_domains = ["tailwindcss.com"]
    start_urls = ["https://tailwindcss.com/docs/aspect-ratio"]

    def parse(self, response):
        for row in response.css('tbody.align-baseline').css('tr'):
            prefix = row.css('td.py-2.pr-2.font-mono.text-xs.leading-6.text-sky-500.whitespace-nowrap::text').get()
            body = ''.join(row.css('td.py-2.pl-2.font-mono.text-xs.leading-6.text-indigo-600.whitespace-pre::text').getall())
            body = [x for x in body.split('\n') if x]
            body = body[0] if len(body) == 1 else body
            if prefix:
                yield {prefix: body}

        next_page = response.css('a.group.ml-auto.flex.items-center::attr(href)').get()
        if next_page != "/docs/typography-plugin":
            yield response.follow(next_page, callback=self.parse)

# scrapy crawl tailwind -O scrape/scrape.json