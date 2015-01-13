package s4mick.dosser;
import java.io.*;


/**
 *
 * @author S4mick
 */
public class Lettura {  ///*// // Lettura stands for "reading" in italian .. and its supposed to simplify the code
   
 InputStreamReader mioIn; 
 BufferedReader miaTastiera;
    

 public Lettura (){
  mioIn=new InputStreamReader(System.in);
  miaTastiera=new BufferedReader(mioIn);    
 }




    public int leggiInt(){ //read int
    int n=-1; //ritorna -1 se non legge niente

try
{
    n=Integer.parseInt(miaTastiera.readLine());
}
catch(Exception e){
System.out.println("Errore");
}

return n;
}
    
////////////////////////////////////////////////////////////////////////////////    
    
   public double leggiFloat(){ // read float
    double n=-1; //ritorna -1 se non legge niente
  
try
{
    n=Float.parseFloat(miaTastiera.readLine());
}
catch(Exception e){
System.out.println("Errore");
}

return n;
}
    
////////////////////////////////////////////////////////////////////////////////    
    
    public String leggiString(){ //read string
    String s=" "; //

try
{
    s=miaTastiera.readLine();
}
catch(Exception e){
System.out.println("Errore");
}

return s;
}
    
///////////////////////////////////////////////////////////////////////////////   
    
public char leggiChar(){ //read char
    char c=' ';
    String s=" ";

try
{
   // s=miaTastiera.readLine();
    
    c=(miaTastiera.readLine()).charAt(0);
}
catch(Exception e){
System.out.println("Errore");
}

return c;
}
    

/////////////////////////////////////////////////////////////////////////////////

     
    
    
    
    

    
    
    
}

    
    
