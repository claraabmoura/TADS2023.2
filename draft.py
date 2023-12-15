from data.download import download_data
from plotnine import ( 
    ggplot, aes, geom_line,
      ggtitle, xlab, ylab )


def plot_line (ticker:str):

    data = download_data(ticker)


    fig = ggplot(
    data = data.reset_index(),
    mapping = aes(x = 'Date' , y = 'Close')
    ) +\
    geom_line() +\
    ggtitle("Dados históricos do BBAS3") +\
    xlab("Data") +\
    ylab("Fechamento")

    return fig

