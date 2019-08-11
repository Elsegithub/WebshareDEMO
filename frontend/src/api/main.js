import a from "axios"
import qs from "qs"
export  function Login(param) {
    console.log(qs.stringify(param))
    let result = a({
        method:'post',
        url:'/api/login/',
        data: qs.stringify(param)
    }).then((response) =>{
      return response.data
    }).catch((Error) =>{
      console.log(Error)
    })
    console.log(result)
    return result
}
