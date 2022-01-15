import java.io.*;
import java.net.*;

public class WebServer  {
   public static void main (String[] args) throws IOException {
      if (args.length != 1) {
         System.out.println("Required arguments: port");
         return;
      }
      int port = Integer.parseInt(args[0]);
      ServerSocket ss = new ServerSocket(port);

      while(true) {
         Socket socket = ss.accept();
         InputStream input = socket.getInputStream();
         BufferedReader br = new BufferedReader(new InputStreamReader(input));

         String str = br.readLine();
         String path = str.split(" ")[1].substring(1);

         OutputStream os = socket.getOutputStream();
         File file = new File(path);
         if (file.exists()) {
            os.write("HTTP/1.1 200 OK\r\n".getBytes());
            os.write("Content-Type:text/html\r\n".getBytes());
            os.write("\r\n".getBytes());
         }else {
            os.write("HTTP/1.1 404 not found\r\n".getBytes());
            os.write("Content-Type:text/html\r\n".getBytes());
            os.write("\r\n".getBytes());
            System.out.println("404 Page Not Found");
            return;
         }

         FileInputStream finput = new FileInputStream(path);
         byte[] bytes = new byte[2048];
         int len = finput.read(bytes);;
         while(len!=-1){
            os.write(bytes,0,len);
            len=finput.read(bytes);
         }
         finput.close();
         socket.close();
      }
   }
}
