import { Link, useLocation } from 'react-router-dom'
import './Header.css'

function Header() {
  const location = useLocation().pathname

  return (
    <header className='header'>
      <div className='container'>
        {location === '/' ? (
          <Link
            to='/signin'
            className='header__link'
          >
            Войти в систему
          </Link>
        ) : (
          <Link
            to='/'
            className='header__link'
          >
            Главная
          </Link>
        )}
      </div>
    </header>
  )
}

export default Header
