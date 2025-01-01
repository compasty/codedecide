import plotly.graph_objects as go
from plotly.subplots import make_subplots

def calc_row_number(with_volume, indicators):
    rows = 2 if with_volume else 1
    if indicators is not None and len(indicators) > 0:
        for indicator in indicators:
            if indicator.separate:
                rows += 1
    return rows

def plot_ohlcv(df, with_volume=True, with_rangeslider=True, title=None, show_legend=False, indicators=None):
    fig = None
    real_title = "Price" if title is None else title
    row_number = calc_row_number(with_volume, indicators)
    if row_number == 1:
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                                             open=df['open'],
                                             high=df['high'],
                                             low=df['low'],
                                             close=df['close'])])
        # 添加指标
        if indicators is not None and len(indicators) > 0:
            for indicator in indicators:
                fig.add_trace(go.Scatter(x=df.index, y=df[indicator.col_name]))
        fig.update_layout(xaxis_rangeslider_visible=with_rangeslider)
        fig.update_layout(title=title, height=500, showlegend=show_legend)
    if with_volume:
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=(real_title, "Volume"), vertical_spacing=0.3)
        fig.add_trace(
            go.Candlestick(x=df.index, open=df['open'], high=df['high'], low=df['low'], close=df['close']),
            row=1, col=1)

        # 添加成交量
        fig.add_trace(go.Bar(x=df.index, y=df['volume'], name="Volume"), row=2, col=1)
        fig.update_layout(xaxis_rangeslider_visible=with_rangeslider)
        fig.update_layout(title=title, height=700, showlegend=show_legend)
    fig.show()