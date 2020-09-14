# COVID-19_detection
Detection of CoVID-19  Coronavirus variability based on clustering algorithm. Final project for data-mining(2020,spring)  
  
  ### 文件说明：  
  一共有四个python文件：Cluster.py, main.py, DBSCAN.py和file_clean.py 和一个原始数据文件usa_county_wise.csv
  
  ### 运行环境：  
  Anaconda3-5.1.0， python 3.7  
  
  ### 需要额外安装的库：  
  不需要，都是Anaconda里自带的  
  
  ### 文件依赖关系：  
  main.py依赖其他三个文件，其他三个彼此独立  
  
  ### 文件作用说明：    

1.usa_county_wise.csv：数据文件  
2.file_clean.py：用于处理csv文件，解决缺省值错误值并生成后面要用的数据格式。 在main.py中被调用。  
3.Cluster.py:定义了Kmeans算法，在main.py中被调用。  
4.DBSCAN.py:定义了DBSCAN算法，在main.py中被调用。  
5.main.py:调用其他文件中的方法完成整个流程，使用时直接运行这个文件即可。  
  
  ### 运行说明：  
  确保所有文件（包括数据文件）都在同一个目录下，运行main.py。我在其他电脑上做过测试，应该是没有问题可以运行的。  
  demo的压缩包里我附带了一个演示视频，如果运行有问题可以看。
