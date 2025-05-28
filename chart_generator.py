import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64


class ChartGenerator:
    def __init__(self, chart_style='seaborn-v0_8-darkgrid'):
        self.chart_style = chart_style
        sns.set_theme(style='darkgrid', font='sans-serif')
    
    def generate_chart(self, df : pd.DataFrame, titulo : str = "Resultado"):
        with plt.style.context(self.chart_style):
            fig, ax = plt.subplots(figsize=(8, 5))
            if df.shape[1] == 2:
                x, y = df.columns
                sns.barplot(x=df[x], y=df[y], ax=ax)
            
            else:
                df.plot(ax=ax)
            ax.set_title(titulo)
            ax.set_ylabel('')
            plt.xticks(rotation=45)
            plt.tight_layout()

            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            plt.close(fig)
            return image_base64
        