### 3.5 小实验1：线性回归练习

（1）不考虑交叉项，根据编程代码可得**prostate_train.txt**线性回归结果为：$\left(\mathrm{R}^{2}, \mathrm{RSS}\right) = (0.626, 36.015)$，对**prostate_test.txt**进行预测，结果评价为：$\left(\mathrm{R}^{2}, \mathrm{RSS}\right) = (0.499, 15.787)$

<img src="report.assets/image-20220312143746475.png" alt="image-20220312143746475" style="zoom:40%;" />

（2）考虑交叉项可能会有更好的效果，在现实中，两个因素可能不会单独作用于一个病理结果，可能是共同作用，相互影响，因此加入交叉项可以从更多的维度上考虑解决问题的模型。

### 3.6 小实验2：线性分类器练习

十折交叉验证法如下：

<img src="report.assets/image-20220312143711288.png" alt="image-20220312143711288" style="zoom:33%;" />

（1）使用logistics回归法，调用sklearn的工具包，并使用十折交叉验证可以拟合出准确率和平均准确率如下：

![image-20220312143845482](report.assets/image-20220312143845482.png)

（2）使用Fisher判别式法则（纯手写，代码见附件），使用十折交叉验证可以拟合出准确率为，平均准确率为：

