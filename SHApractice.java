import java.security.*;

public class SHApractice{
    public static void main(String[] args){

        char[] hexDigits = "0123456789ABCDEF".toCharArray();
        StringBuilder hexString = new StringBuilder();
        try{
        MessageDigest md = MessageDigest.getInstance("SHA-1");
        System.out.println("Algorithm :"+md.getAlgorithm());
        System.out.println("Provider : "+md.getProvider());
        System.out.println("Digest Length :"+md.getDigestLength());
        String input = "SRINADH CHINTAKINDI";
        md.update(input.getBytes());
        byte[] output = md.digest();
        for (byte b: output){
            hexString.append(hexDigits[(b<<4)& 0x0F]);
            hexString.append(hexDigits[b&0x0F]);
        }
        

        System.out.println("SHA-1 bytes hash value: "+output);
        System.out.println("SHA-1('"+input+"')="+hexString.toString());
        }
        catch(NoSuchAlgorithmException e){
            System.err.println("Exception :"+e.getMessage());
        }
    }
    
}