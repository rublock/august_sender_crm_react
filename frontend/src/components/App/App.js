import Header from '../Header/Header'
import Footer from '../Footer/Footer'
import SignIn from '../SignIn/SignIn'

import Main from '../Main/Main'

import { Routes, Route } from 'react-router-dom'

import './App.css'

function App() {
  return (
    <>
      <Header />
      <div>
        <Routes>
          <Route
            path='/signin'
            element={<SignIn />}
          />
          <Route
            path='/'
            element={<Main />}
          />
        </Routes>
      </div>

      <Footer />
    </>
  )
}

export default App
