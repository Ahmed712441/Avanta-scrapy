import scrapy
from ..items import AvantaItem
# from scrapy_splash import SplashRequest
from scrapy.http import Request

class AvantaSpider(scrapy.Spider):



    name = 'avanta'
    start_urls = ['https://www.avantgardevegan.com/recipes/']

    
    @staticmethod
    def remove(list,strings):
        return_list = []
        for s in list:
            if s in strings:
                continue
            return_list.append(s)
        return return_list
    
    @staticmethod
    def unique(list):
        return_list = []
        count = 2
        for s in list:
            if not s in return_list:
               return_list.append(s) 
            else :
                return_list.append(s+str(count))
                count+=1
        return return_list
            
    def parse(self, response):
        
        urls = response.css('.entry-title a::attr(href)').extract()

        titles = response.css('.entry-title a::text').extract()

        images = response.css('.wp-post-image::attr(src)').extract()


        categories_selector = response.css('.entry-recipe-categories')
        categories = []
        for category in categories_selector :
	
            strings = category.css('::text').extract()
            categories.append( ''.join(strings) )

        for i in range(len(urls)):

            yield Request(urls[i],callback=self.scrape_inner,meta=dict(url=urls[i],title=titles[i],image=images[i],category=categories[i]))
            # yield SplashRequest(urls[i],callback=self.scrape_inner,args={'wait': 10},meta=dict(url=urls[i],title=titles[i],image=images[i],category=categories[i]))

        for page_num in range(1,14):
            url = f'https://www.avantgardevegan.com/recipes/?sf_paged={page_num}'
            yield Request(url,callback=self.parse)
        
    def scrape_inner(self,response):

        item = AvantaItem()

        item['url'] =response.meta['url']
        item['title'] =response.meta['title']
        item['image'] =response.meta['image']
        item['category'] =response.meta['category']
        item['stats'] = AvantaSpider.remove(response.css('.entry-quick-info .col-md::text').extract(),[' ','\xa0'])
        
        ing_titles = response.css('b::text').extract()
        method_titles =  response.css('strong').css('::text').extract()[:-3]
        method_titles = AvantaSpider.remove(method_titles,[' ','\xa0'])	
        # method_titles = AvantaSpider.unique(method_titles)
        if (len(ing_titles) == 0):
            ing_titles = method_titles
        ing_titles = AvantaSpider.remove(ing_titles,[' ','\xa0'])
        # ing_titles = AvantaSpider.unique(ing_titles)
        # ingredients = response.css('.recipe-ingredients .p1').css('::text').extract()
        # if len(ingredients)==0:
        check_list = response.css('.recipe-ingredients a::text').extract()
        if (len(check_list) == 0)  or ( (len(check_list) == 1) and (check_list[0] == '(recipe here)') ):
            ingredients = response.css('.recipe-ingredients p').css('::text').extract()
            ingredients = AvantaSpider.remove(ingredients,[' ','\xa0'])
        else :
            ing_selector = response.css('.recipe-ingredients p')
            ingredients = []
            for ing in ing_selector:
                ingredients.append(' '.join(AvantaSpider.remove(ing.css('::text').extract(),[' ','\xa0'])))

        ingredients_dict=dict()
        try:
            if  not ingredients[0] in ing_titles:
                key = 'default'
                ingredients_dict[key] = []
        except:
            key = 'default'
            ingredients_dict[key] = []


        for i in range(len(ingredients)):
            if(ingredients[i] in ing_titles):
                key = ingredients[i]
                try: 
                    ingredients_dict[key] 
                    key = key+'_'
                except:
                    pass
                ingredients_dict[key] = []
                continue
            ingredients_dict[key].append(ingredients[i])

        item['ingredients'] = ingredients_dict


        try:
            
            id = response.css('.video-link::attr(data-videoid)').extract()[0]
            item['video'] = f'https://www.youtube.com/watch?v={id}'
        except:
            item['video'] = None

        try :
            item['about'] = response.css('.recipe-introduction p::text').extract()
        except:
            item['about'] = None

        # method_titles =  response.css('strong').css('::text').extract()[:-3]
        # method_titles = AvantaSpider.remove(method_titles,[' ','\xa0'])
        # methods = response.css('.recipe-method .p1').css('::text').extract()
        # if len(methods) == 0:
        methods = response.css('.recipe-method p').css('::text').extract()
        if len(methods) == 0:
            try:
                methods = response.css('li::text').extract()[5:-5]
            except:
                pass
        methods = AvantaSpider.remove(methods,[' ','\xa0'])
        methods_dict=dict()
        try:
            if not methods[0] in method_titles :
                key2 = 'default'
                methods_dict[key2] = []
        except:
            key2 = 'default'
            methods_dict[key2] = []
            

        for i in range(len(methods)):
            if(methods[i] in method_titles):
                key2 = methods[i]
                try: 
                    methods_dict[key2]
                    key2 = key2+'_' 
                except:
                    pass
                methods_dict[key2] = []
                continue
            methods_dict[key2].append(methods[i])

        item['method'] = methods_dict

        yield item