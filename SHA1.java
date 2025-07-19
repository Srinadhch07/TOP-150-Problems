import java.security.*;
public class SHA1{
    public static void main(String[] args){
        try{
        MessageDigest md = MessageDigest.getInstance("SHA-1");
        String input = "Srinadh Chintakindi";
        md.update(input.getBytes());
        byte[] output = md.digest();
        System.out.println("SHA-1 Hash Value('"+input+"')="+output);
        }
        catch(NoSuchAlgorithmException e){
            System.err.println("Exception"+e.getMessage());
        }}}