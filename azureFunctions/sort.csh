using System;
using System.Net;
using System.Collections.Generic;
using System.Collections;


public static async Task<HttpResponseMessage> Run(HttpRequestMessage req, TraceWriter log)
{
    log.Info("C# HTTP trigger function processed a request.");

    // Get request body
    dynamic data = await req.Content.ReadAsAsync<object>();
    //name = name ?? data?.name;

    string num_string = data.num;


    // parse query parameter
    // string num_string = req.GetQueryNameValuePairs()
    //     .FirstOrDefault(q => string.Compare(q.Key, "num", true) == 0)
    //     .Value;
    
    long num = Int64.Parse(num_string);
    log.Info("parsed num: "+ num);

    Random rand = new Random();
    List<int> intList = new List<int>();

    for(long i=0;i<num;i++) {
        intList.Add(rand.Next(10000));
    }
    
    //Sort
    intList.Sort();


    // Set name to query string or body data
    //name = name ?? data?.name;

    return intList == null
        ? req.CreateResponse(HttpStatusCode.BadRequest, "Please pass a name on the query string or in the request body")
        // : req.CreateResponse(HttpStatusCode.OK, "Hello " + string.Join(",", intList));
        : req.CreateResponse(HttpStatusCode.OK, string.Join(",", intList)+"\n");
}
