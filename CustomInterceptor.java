package com.flumetest;

import java.util.Iterator;
import java.util.List;
import java.util.Map;

import org.apache.flume.Context;
import org.apache.flume.Event;
import org.apache.flume.interceptor.Interceptor;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;

public class CustomInterceptor implements Interceptor
{
  
  private final String partitionKey = "key";

  @Override
  public void close()
  {

  }

  @Override
  public void initialize()
  {

  }

  @Override
  public Event intercept(Event event) 
  {
     
     String uuidServerStr = "";
     String uuidClientStr = "";
     String uuidStr = "";
     
     String eventBody = new String(event.getBody());
     int cookieStartIndex = eventBody.indexOf("UUIDS:")+"UUIDS:".length();
    	
     System.out.println("eventBody === "+eventBody); 
     int i = cookieStartIndex;
     char myChar = '\0';
     
     myChar = eventBody.charAt(i);
     while(myChar != '-' && myChar != ' ')
     {
	uuidServerStr += myChar;
	myChar = eventBody.charAt(++i);
     }

     if(myChar == '-')
	i++;
	
     i++;

     i += "UUIDC:".length();
	
     myChar = '\0'; 
     myChar = eventBody.charAt(i);

     while(myChar != '-' && myChar != ' ')
     {
        uuidClientStr += myChar;
        myChar = eventBody.charAt(++i);
     }
                  
     uuidStr = uuidClientStr;

     if (uuidStr == "")
	uuidStr = uuidServerStr;   

     Map headers = event.getHeaders();
     headers.put(partitionKey, uuidStr);
                
     event.setHeaders(headers);
     try
     {
	File statText = new File("./output.txt");
        FileOutputStream is = new FileOutputStream(statText);
        OutputStreamWriter osw = new OutputStreamWriter(is);    
        Writer w = new BufferedWriter(osw);
        w.write("eventBody  = ");
	w.write(eventBody);
	w.write("\n \n \n");
	w.write("uuidStr = ");
	w.write(uuidStr);
        w.close();
     } catch (IOException e) {
            System.err.println("Problem writing to the file statsTest.txt");
     }
     System.out.println("######################### uuidStr = "+uuidStr);
                
     return event;
  }

  @Override
  public List intercept(List events)
  {
     for (Iterator iterator = events.iterator(); iterator.hasNext();)
     {
       Event next = intercept((Event)iterator.next());
       if (next == null)
       {
          iterator.remove();
       }
     }

     return events;
  }

  public static class Builder implements Interceptor.Builder
  {
     @Override
     public void configure(Context context)
     {
     }

     @Override
     public Interceptor build() 
     {
        return new CustomInterceptor();
     }
   }
}
