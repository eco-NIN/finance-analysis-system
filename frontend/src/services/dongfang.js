import axios from 'axios'

export const fetchPrediction = (params) => {
  return axios.get('/api/v1/prediction/predict', { params })
}
