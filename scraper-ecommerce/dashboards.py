import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('product_list.csv')

df['product_price_num'] = df['product_price'].str.replace('$', '').astype(float)

app = dash.Dash(__name__)

fig1 = px.histogram(df, x='product_price_num', nbins=30, title='Distribuição de Preços', labels={'product_price_num': 'Preço ($)'})
fig2 = px.box(df, y='product_price_num', title='Boxplot dos Preços dos Produtos', labels={'product_price_num': 'Preço ($)'})

top10_preco = df.nlargest(10, 'product_price_num')
fig3 = px.bar(top10_preco.sort_values('product_price_num'),
              x='product_price_num',
              y='product_name',
              orientation='h',
              title='Top 10 produtos mais caros',
              labels={'product_price_num': 'Preço ($)', 'product_name': 'Produto'})

top10_review = df.nlargest(10, 'product_review')
fig4 = px.bar(top10_review.sort_values('product_review'),
              x='product_review',
              y='product_name',
              orientation='h',
              title='Top 10 produtos mais bem avaliados',
              labels={'product_review': 'Avaliações', 'product_name': 'Produto'})   

app.layout = html.Div(children = [
    html.H1(children='Dashboards de Produtos'),

    dcc.Graph(
        id='price-histogram',
        figure=fig1
    ),

    dcc.Graph(
        id='price-boxplot',
        figure=fig2
    ),

    dcc.Graph(
        id='top10-products-price-bar',
        figure=fig3
    ),

    dcc.Graph(
        id='top10-products-review-bar',
        figure=fig4
    )
])

if __name__ == '__main__':
    app.run(debug=True)