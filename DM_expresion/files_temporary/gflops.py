def main():
    sum=0
    list3=[6.18744,]
    list3.sort()
    list2=list3[50:249]
    for i in list2:
        sum+=i
    gflops=sum/200
    with open("./files_temporary/data_out_cpp.txt","at") as f:
        print(gflops,sep="",end=" ",file=f)
if __name__ == "__main__":
    main()
33.427,11.5092,4.96566,34.5606,11.6082,16.7058,6.3401,0.724073,6.26757,4.13569,6.19503,4.12847,2.03406,17.0969,4.07692,5.86204,15.8953,0.719816,5.89196,4.08025,3.88293,32.6896,2.92364,5.40075,12.0441,5.98217,6.16556,0.707016,6.27877,18.0014,17.7146,6.17192,0.713969,6.23005,6.23919,6.22142,6.13755,0.468577,6.19241,6.18609,