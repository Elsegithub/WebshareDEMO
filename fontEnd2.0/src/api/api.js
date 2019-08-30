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
export const search_list = () => {
    return axios.request({
        method: 'get',
        params: {},
        url: '/api/test_list/',
        data: {}
    })
}

export const search_geciList = () => {
    return axios.request({
        method: 'post',
        params:{},
        url: '/api/search_geciList/',
        data: {}
    })
}