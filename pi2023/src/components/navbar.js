import React from "react";


export default class Navbar extends React.Component{
	static styleTypes={
		mobileStanding:{},
		mobileResting:{},
		tabletStanding:{},
		tabletResting:{},
		desktop:{}
	}
	constructor(props){
		super(props);
		this.childContents=props.contents;
		this.h=Number(props.height);
	}

	margin(h){return this.h/2-h/2}
	part(p){return this.h*p}

	render(){
		let x=-1,
			items=[],
			divStyle={position:'fixed',width:'100%',height:this.h},
			navStyle={listStyle:'none',display:'inline-block',height:this.part(0.6),marginTop:this.margin(this.part(0.6)),marginLeft:this.part(0.5),float:'right'},
			imgStyle={display:'inline-block',height:this.part(0.8),marginTop:this.margin(this.part(0.8)),float:'left'},
			listStyle={display:'inline-block',marginRight:this.part(0.5)}

		while(++x<this.childContents.length){
			items.push(<li key={x} style={listStyle}>{this.childContents[x]}</li>)
		}
		return (
			<>
			<div style={divStyle}>
				<img style={imgStyle} src="/logo.png"/>
				<nav style={navStyle}>
					{items}
				</nav>
			</div>
			<div style={{height:`${this.h}px`}}></div>
			</>

		);
	}

}
