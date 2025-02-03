import pandas as pd
from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)





import statsmodels.formula.api as smf
model = smf.ols('MPG~WT+VOL+SP+HP',data=df).fit()



model.params


print(model.tvalues, '\n', model.pvalues)


(model.rsquared,model.rsquared_adj)




ml_v = smf.ols('MPG ~ VOL', data=df).fit()
print(ml_v.tvalues, '\n', ml_v.pvalues)