from urlextract import URLExtract
extractor=URLExtract()
from wordcloud import WordCloud
def help_to_fetch(selected_data, tabel):
    words = []
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    for i in tabel["message"]:
        words.extend(i.split())
    num = tabel.shape[0]
    links = []
    for i in tabel["message"]:
        links.extend(extractor.find_urls(i))

    msg=tabel[tabel["message"]=="<Media omitted>"].shape[0]



    return num, words,msg,len(links)
def most_busy_users(tabel):
    pp = tabel["sender"].value_counts()
    percentage_df = (tabel["sender"].value_counts(normalize=True) * 100).reset_index()
    percentage_df.columns = ["user", "percentage"]

    return pp,percentage_df
def create_word_cloud(selected_data, tabel):
    if selected_data != "Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    wc=WordCloud(height=500,width=500,min_font_size=10,background_color="white")
    neww=wc.generate(tabel["message"].str.cat(sep=" "))
    return neww
