import axios from 'axios'

export function fetchPredictionResults(formData) {
    return axios
    .post('/api/v1/prediction/tushare_predict',formData)
    .then((res) => res.data)
}