    
    
def  news_data() :

    file_news = open('file_news.txt', 'r')
    i = 0
    title = ''
    short_story = ''
    full_story = ''
    news_list_data = {}
    for line in file_news:
        if line != 'endtitle\n':
            title += line[0:-1] 
        if line == 'title\n':
            # print(line)
            title = ''
            i = 0
        if line == 'endtitle\n':
            news_list_data.update({title:[]})
            title1 = title

        if line != 'endshort_story\n':
            short_story += line[0:-1] 
        if line == 'short_story\n':
            # print(line)
            short_story = ''
            i = 0
        if line == 'endshort_story\n':
            news_list_data[title1]=[short_story]

        if line != 'endfull_story\n':
            full_story += line[0:-1] 
        if line == 'full_story\n':
            # print(line)
            full_story = ''
            i = 0
        if line == 'endfull_story\n':
            news_list_data[title1].append(full_story)
    return news_list_data

    # print(news_list_data)
