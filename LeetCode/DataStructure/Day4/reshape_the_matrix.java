class Solution {
    public static int[] Two2One(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[] array = new int[rows*cols];
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                array[i * cols + j] = mat[i][j];
            }
        }
        return array;
    }
    public static void printArray1D(int[] array){
        for(int i = 0; i < array.length; i++){
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }
    public static void printArray2D(int[][] array){
        for(int i = 0; i < array.length; i++){
            for(int j = 0; j < array[i].length; j++){
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int[][] One2Two(int[] array){
        int n = array.length / 2;
        int[][] result = new int[n][n];
        for(int i = 0; i < array.length; i++){
            result[i/n][i%n] = array[i];
        }
        return result;
    }
    public static void main(String[] args) {
        int[][] array = {{1,2}, {3,4}};
        int[] result = Two2One(array);
        printArray1D(result);
        // =============================================
        int[] ar = {6, 7, 8, 9};
        int[][] r = One2Two(ar);
        printArray2D(r);

    }
}