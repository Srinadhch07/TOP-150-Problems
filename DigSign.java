import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;
import java.util.Base64;

public class DigSign {
    public static void main(String[] args) throws Exception {
        // Generate a KeyPair using RSA
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(1024);
        KeyPair keyPair = kpg.genKeyPair();

        // Data to sign
        byte[] data = "Sample Text".getBytes("UTF8");

        // Create a Signature instance with MD5 and RSA
        Signature sig = Signature.getInstance("MD5WithRSA");
        
        // Sign the data
        sig.initSign(keyPair.getPrivate());
        sig.update(data);
        byte[] signatureBytes = sig.sign();
        System.out.println("Signature: \n" + Base64.getEncoder().encodeToString(signatureBytes));

        // Verify the signature
        sig.initVerify(keyPair.getPublic());
        sig.update(data);
        System.out.println("Signature verified: " + sig.verify(signatureBytes));
    }
}
