'use client'
import Navbar from "@/components/navbar"

export default function Home() {
  return (
    <div>
			<Navbar height={55} contents={['Página Inicial','Sobre','Contato']}/>
			<p>this is the main project!!!</p>
		</div>
  )
}
