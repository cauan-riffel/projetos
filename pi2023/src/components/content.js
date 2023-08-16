import React from "react";


export default class MainContent extends React.Component{
	static DEFAULT_HEIGHT=600;
	constructor(props){
		super(props);
		//'specials'
		this.id=props.id||'guest';
		this.type=props.type||'none';
		this.subType=props.subtype||'normal';
		// contents
		this.title=props.title||`give ${this.id} some title!!!`;
		this.subTitle=props.subTitle||`give ${this.id} some subtitle!!!`;
		this.img=props.img||'/darkNone.png';
		//values
		this.height=props.height||MainContent.DEFAULT_HEIGHT;
		this.color=props.color||'#dbc2cf';
		this.margin=props.margin||55;
	}

	render(){
		if(this.type=='centered'){
			if(screen.availWidth>888)return(<MainCentered
				//contents
				title={this.title}
				subtitle={this.subTitle}
				img={this.img}
				//values
				height={this.height}
				//'specials'
				id={this.id}
			/>);
		}else if(this.type=='reversed'){
			return(<MainLateral
				//contents
				title={this.title}
				subtitle={this.subTitle}
				img={this.img}
				//values
				height={this.height}
				color={this.color}
				margin={this.margin}
				//'specials'
				subtype={this.subType}
				id={this.id}
			/>);;
		}else{
			return(<p>Type not defined!</p>);
		}
	}
}


class MainCentered extends React.Component{
	constructor(props){
		super(props);

		this.btn=props.button||false;

		this.height=props.height;
		this.id=props.id;

		this.title=props.title;
		this.subTitle=props.subtitle;
		this.img=props.img;

	}

	getMargin(height,elementHeight){
		return (elementHeight||this.height)/2 - height/2;
	}

	getPercent(percentage){
		return this.height*percentage;
	}

	render(){
		const mainDivStyle={
			width:'100%',backgroundImage:`url(${this.img})`,
			height:this.height,
		}
		const subDivStyle={
			width:'60%',marginLeft:'20%',
			marginTop:this.getMargin(this.getPercent(0.6)),float:'left'
		}
		const h2Style={
			textAlign:'center',fontSize:'2.5rem',
			color:'white'
		}
		const pStyle={
			textAlign:'center',fontSize:'1.2rem',
			color:'white'
		}


		return (
			<div id={this.id} style={mainDivStyle}>
				<div style={subDivStyle}>
					<h1 style={h2Style}>{this.title}</h1>
					<p style={pStyle}>{this.subTitle}</p>
					{/*{(this.btn)?<button>leia mais</button>:''}*/}
				</div>
			</div>
		);
	}
}

class MainLateral extends React.Component{
	constructor(props){
		super(props);
		//'specials'
		this.id=props.id||'guest';
		this.type=props.type||'none';
		this.subtype=props.subtype||'normal';
		// contents
		this.title=props.title;
		this.subTitle=props.subtitle;
		this.img=props.img||'/darkNone.png';
		//values
		this.height=props.height;
		this.color=props.color;
		this.margin=props.margin;
	}

	getMargin(height,elementHeight){
		return (elementHeight||this.height)/2 - height/2;
	}

	getPercent(percentage){
		return this.height*percentage;
	}

	render(){
		const mainStyle={
			backgroundColor:this.color,height:this.height
		}
		const childStyle={
		}
		const imgStyle={
			display:'inline-block',float:((this.subtype=='normal')?'right':'left'),width:this.getPercent(0.8),marginTop:this.getMargin(this.getPercent(0.8)),
			marginRight:(this.subtype=='normal')?this.margin:'',marginLeft:(this.subtype=='normal')?'':this.margin
		}
		const divStyle={
			display:'inline-block',float:((this.subtype=='normal')?'left':'right'),
			marginTop:this.getMargin(this.getPercent(0.8)),
			marginRight:(this.subtype=='normal')?'':this.margin,marginLeft:(this.subtype=='normal')?this.margin:'',textAlign:'center',height:this.getPercent(0.8)
		}
		const pStyle={
			textAlign:'center',maxWidth:this.getPercent(1),marginTop:25
		}
		const h2Style={
			fontSize:'2.5rem',marginTop:this.getMargin(this.getPercent(0.8))
		}
		const mainPart=[
			<img key={0} style={imgStyle} src={this.img}/>,
			<div key={1} style={divStyle}>
				<h2 style={h2Style}>{this.title}</h2>
				<p style={pStyle}>{this.subTitle}</p>
			</div>
		];


		return(
			<div id={this.id} style={mainStyle}>
				<div style={childStyle}>
					{mainPart}
				</div>
			</div>
		);
	}
}
