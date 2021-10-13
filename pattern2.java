public class pattern2 {
//Hill slope pattern
    public static void main(String Agrs[]){
        int rows=10;
        int b=rows;
        for(int i=1;i<=rows;i++){
            for(int j=1;j<=100;j++){
                if(j==i*i){
                    System.out.print("*");
                    b--;
                }else{
                    System.out.print(" ");
                             }

            }System.out.println("");
        }
    }
}