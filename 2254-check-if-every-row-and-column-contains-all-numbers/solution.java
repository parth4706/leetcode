class Solution {
    public boolean checkValid(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            int arr[] = new int[matrix.length];
            for (int j = 0; j < matrix.length; j++) {
                if (arr[matrix[i][j] - 1] == 1) {
                    return false;
                }
                arr[matrix[i][j] - 1]++;
            }
        }
        for (int j = 0; j < matrix.length; j++) {
            int arr[] = new int[matrix.length];

            for (int i = 0; i < matrix.length; i++) {
                if (arr[matrix[i][j] - 1] == 1) {
                    return false;
                }
                arr[matrix[i][j] - 1]++;
            }
        }

        return true;
    }
}
