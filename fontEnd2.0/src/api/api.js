import axios from '@/libs/api.request'
import qs from 'qs'

export const testPost = postData => {
    return axios.request({
        method: 'post',
        params: {},
        url: '/api/test/',
        data: qs.stringify(postData)
    })
}