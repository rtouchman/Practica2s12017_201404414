/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edd.webclient;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

/**
 *
 * @author rt
 */
public class Client {

    public static OkHttpClient webClient = new OkHttpClient();
    
    public static void addToList(String data){
        
        RequestBody body = new FormEncodingBuilder()
                .add("data", data)
                .build();
        
        String method = "List/add";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void searchInList(String data){
        
        RequestBody body = new FormEncodingBuilder()
                .add("data", data)
                .build();
        
        String method = "List/search";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void removeFromList(String index){
        
        RequestBody body = new FormEncodingBuilder()
                .add("index", index)
                .build();
        
        String method = "List/remove";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void reportList(){
        
        String method = "List/report";
        System.out.println(Client.getString(method));
        
    }
    
    public static void enqueue(String data){
        
        RequestBody body = new FormEncodingBuilder()
                .add("data", data)
                .build();
        
        String method = "Queue/enqueue";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void dequeue(){
        
        String method = "Queue/dequeue";
        
        System.out.println(Client.getString(method));
        
    }
    
    public static void reportQueue(){
        
        String method = "Queue/report";
        
        System.out.println(Client.getString(method));
        
    }
    
    public static void push(String data){
        
        RequestBody body = new FormEncodingBuilder()
                .add("data", data)
                .build();
        
        String method = "Stack/push";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void pop(){
        
        String method = "Stack/pop";
        
        System.out.println(Client.getString(method));
        
    }
    
    public static void reportStack(){
        
        String method = "Stack/report";
        
        System.out.println(Client.getString(method));
        
    }
    
    public static void insert(String mail){
        
        String data[] = mail.split("@");
        
        RequestBody body = new FormEncodingBuilder()
                .add("domain", data[1])
                .add("name", data[0])
                .build();
        
        String method = "Matrix/insert";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void searchByDomain(String domain){
        
        RequestBody body = new FormEncodingBuilder()
                .add("domain", domain)
                .build();
        
        String method = "Matrix/search/domain";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void searchByLetter(String letter){
        
        RequestBody body = new FormEncodingBuilder()
                .add("letter", letter)
                .build();
        
        String method = "Matrix/search/domain";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void delete(String mail){
        
         String data[] = mail.split("@");
        
         RequestBody body = new FormEncodingBuilder()
                .add("domain", data[1])
                .add("name", data[0])
                .build();
        
        String method = "Matrix/delete";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static void reportMatrix(){
        
        String method = "Matrix/report/headers";
        
        System.out.println(Client.getString(method));
        
    }
    
    public static void reportMatrix(String mail){
        
         String data[] = mail.split("@");
        
         RequestBody body = new FormEncodingBuilder()
                .add("domain", data[1])
                .add("name", data[0])
                .build();
        
        String method = "Matrix/report/node";
        
        System.out.println(Client.getString(method, body));
        
    }
    
    public static String getString(String method, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + method);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(edd.webclient.Client.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            java.util.logging.Logger.getLogger(edd.webclient.Client.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
    public static String getString(String method) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + method);
            Request request = new Request.Builder().url(url).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(edd.webclient.Client.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            java.util.logging.Logger.getLogger(edd.webclient.Client.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
