import matplotlib.pyplot as plt
import seaborn as sb
iris=sb.load_dataset("iris")
sb.boxplot(x="species",y="petal_length",data=iris,width=.2)
print(sb)
