import java.security.*;

public class SHA {

    public static void main(String[] args) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-1"); 
            // System.out.println("Algorithm =" + md.getAlgorithm());
            // System.out.println("Provider =" + md.getProvider());
            // System.out.println("DigestLength ="+md.getDigestLength());
            // System.out.println("Class ="+md.getClass());

            String[] inputs = {"", "abc", "abcdefghijklmnopqrstuvwxyz","Srinadh"};
            for (String input : inputs) {
                md.update(input.getBytes()); // Update the hash with the input bytes
                byte[] output = md.dig      est();   // Calculate the final hash
                System.out.println("SHA-1 bytes HASH :"+output);
                //System.out.println("SHA-1('" + input + "')=" + bytesToHex(output)); 
            }
        } catch (NoSuchAlgorithmException e) {
            System.err.println("Exception: " + e.getMessage()); 
        }
    }

    // public static String bytesToHex(byte[] b){
    //     char[] hexDigits = "0123456789ABCDEF".toCharArray();
    //     StringBuilder hexString = new StringBuilder();
    //     for(byte by:b){
    //         hexString.append(hexDigits[(by<<4)& 0x0F]);
    //         //hexString.append(hexDigits[by&0x0F]);
    //     }
    //     return hexString.toString();
    // }
}