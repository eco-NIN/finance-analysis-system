// frontend/src/services/crawler.js
import axios from 'axios'

export function getStockList() {
    return axios
    .get('/api/v1/crawler/stock_list')
    .then((res) => res.data)
}


export const fetchStockBasic = () => {
  return axios
    .get('/api/v1/crawler/fetch_stock_basic')
    .then((res) => res.data)
}