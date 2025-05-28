import axios from 'axios'

export function fetchPredictionResults(formData) {
    return axios
    .post('/api/v1/prediction/predict',formData)
    .then((res) => res.data)
}