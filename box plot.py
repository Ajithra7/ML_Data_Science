import matplotlib.pyplot as plt
import seaborn as sb
iris=sb.load_dataset("iris")
sb.boxplot(x="species",y="petal_width",data=iris)
print(sb)
